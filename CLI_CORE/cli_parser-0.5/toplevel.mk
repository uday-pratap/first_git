# Toplevel make rules
#
# This file is the top-level make rules for all targets. Each target
# is uniquely defined by (BS or MS, platform); e.g. (BS, simulation).
# For each target, there should be a Makefile.[target]. Each target
# top-level Makefile should have the following variables:
#
# PLATFORM - Define a target string; e.g. bs_sim
#
# MODULE_LIST - A list of module directories. Each module directory
#     will produce a [module].a library; e.g. tlv.a.
#
# BIN_LIST - A list of application directories. Each directory will
#     produce an application binary.
#
# TEST_LIST - A list of test program directories. Each directory will
#     produce a  test program. This variable is optional. But usually,
#     each module will have its own test programs.
#
# To add a new target, simply create a Makefile.[target] with the
# variables listed above. The last line should be "include toplevel.mk".
# Also, create a target in mac/Makefile.
#


ifeq ("$(OUTDIR)", "")
OUTDIR = .
endif

ifeq ("$(DEBUG)", "TRUE")
BUILDDIR = $(OUTDIR)/build/$(PLATFORM)_dbg
else
BUILDDIR = $(OUTDIR)/build/$(PLATFORM)
endif

DIR_LIST = $(patsubst %,%.PHONY,$(MODULE_LIST) $(BIN_LIST) $(LIB_LIST))

CLEAN_LIST = $(patsubst %,%.PHONY_CLEAN,$(MODULE_LIST))

$(BUILDDIR):
	@echo "MKDIR $@"
	mkdir -p $(BUILDDIR)/obj $(BUILDDIR)/bin $(BUILDDIR)/lib

$(DIR_LIST):
	@echo "MAKE $(basename $@)"
	$(MAKE) PLATFORM=$(PLATFORM) MODULE=$(basename $@) DEBUG="$(DEBUG)" LIBRARY=$(LIBRARY) -C $(basename $@)/src all

$(TEST_LIST):
	@echo "MAKE TEST $(dir $@):$(notdir $@)..."
	$(MAKE) PLATFORM=$(PLATFORM) MODULE=$(dir $@) DEBUG="$(DEBUG)" -C $(dir $@)src -f Makefile.$(notdir $@) all

$(CLEAN_LIST):
	@echo "CLEAN $(basename $@)"
	$(MAKE) PLATFORM=$(PLATFORM) MODULE=$(basename $@) DEBUG="$(DEBUG)" LIBRARY=$(LIBRARY) -C $(basename $@)/src clean

bin: $(BUILDDIR) $(DIR_LIST)

all: bin $(TEST_LIST)

NIGHTLY_DIR = ./scripts/nightly
NIGHTLY_UNIT_TEST = env PYTHONPATH=$(NIGHTLY_DIR)/sql_driver $(NIGHTLY_DIR)/unit_tests/nightly_run.py

tests: all
	$(NIGHTLY_UNIT_TEST) --bin-dir=$(BUILDDIR)/bin $(notdir $(TEST_LIST))

tests_logged: all
	$(NIGHTLY_UNIT_TEST) --user=root --project=CLI_Parser --target=$(PLATFORM) --bin-dir=$(BUILDDIR)/bin $(TEST_LIST)

clean: $(CLEAN_LIST)
	@echo "CLEAN $(notdir $(BUILDDIR))"
	rm -fr $(BUILDDIR)
