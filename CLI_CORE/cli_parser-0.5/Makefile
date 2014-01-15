# Top-level Makefile for CLI Parser


all: unix

# Individual targets
unix:
	$(MAKE) -f Makefile.unix all

# This target does everything that unix_tests does and logs an entry
# in a MySQL database. To run this target, you must install Python MySQL
# package.
unix_tests_logged: unix
	$(MAKE) -f Makefile.unix tests_logged

# Clean targets
unix_clean:
	$(MAKE) -f Makefile.unix clean
	$(MAKE) -f Makefile.unix DEBUG=TRUE clean

clean: unix_clean
	rm -fr build/ html/

