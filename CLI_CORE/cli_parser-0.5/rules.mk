# Makefile rules for CLI Parser


# Define a root build directory based on the platform
ifeq ("$(OUTDIR)", "")
  OUTDIR = .
endif

ifeq ("$(PLATFORM)", "")
  # Without a platform defined, just use local directory
  BUILDDIR = .
  OBJDIR   = .
  BINDIR   = .
  LIBDIR   = .
else
  ifeq ("$(DEBUG)", "TRUE")
    BUILDDIR = $(OUTDIR)/$(SRC_BASE)/build/$(PLATFORM)_dbg
  else
    BUILDDIR = $(OUTDIR)/$(SRC_BASE)/build/$(PLATFORM)
  endif
  # Define the object, binary, and library directory
  OBJDIR = $(BUILDDIR)/obj/$(MODULE)
  BINDIR = $(BUILDDIR)/bin
  LIBDIR = $(BUILDDIR)/lib
endif

# Update compilation flags based on DEBUG
ifeq ("$(DEBUG)", "TRUE")
  CFLAGS += $(ETCFLAGS) -Wall -g -Werror -O0
else
  CFLAGS += $(ETCFLAGS) -Wall -g -Werror -O2
endif

# Add a bunch of default include path
SRC_INC += -I. -I../inc \
	   -I$(SRC_BASE)/inc \
	   -I$(SRC_BASE)/pool/inc \
	   -I$(SRC_BASE)/queue/inc \
	   -I$(SRC_BASE)/heap/inc \
	   -I$(SRC_BASE)/timer/inc \
	   -I$(SRC_BASE)/fsm/inc
SRC_OBJ = $(patsubst %.c,$(OBJDIR)/%.o,$(SRC_FILES))
SRC_DEP = $(patsubst %.c,$(OBJDIR)/%.d,$(SRC_FILES))

# Include the list of dependency files
-include $(SRC_DEP)


# Implicit rule to compile all source files
$(OBJDIR)/%.o:%.c
	@echo "  DEP     $<..."
	$(CC) $(CFLAGS) -MM $(SRC_INC) -MF $(patsubst %.o,%.d,$@) -MT $@ $< 
	@echo "  COMPILE $<..."
	$(CC) -c $(CFLAGS) $(SRC_INC) $< -o $@
ifneq ("$(LIBRARY)", "")
	@echo "  ARCHIVE $(notdir $@)..."
	$(AR) rcs $(LIBDIR)/$(LIBRARY) $@
endif

all: lib bin

dir: $(OBJDIR)

lib: dir $(SRC_OBJ)

bin: dir $(BINDIR)/$(SRC_BIN)

$(OBJDIR):
	@echo "  MKDIR obj/$(notdir $@)..."
	mkdir -p $@

# Build test programs
ifneq ("$(SRC_BIN)", "")
$(BINDIR)/$(SRC_BIN): $(SRC_OBJ) $(patsubst %,../../%,$(AR_LIST))
	@echo "  LINK    $(notdir $@)..."
	$(CC) $(SRC_OBJ) $(patsubst %,../../%,$(AR_LIST)) ../src/lib/libparser_core.a -o $(BINDIR)/$(SRC_BIN) $(SRC_LIB)
endif


clean: local_clean
	rm -f $(SRC_BIN) *.o $(SRC_BIN).exe 
	rm -f *.d

local_clean:
