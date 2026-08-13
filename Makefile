.DEFAULT_GOAL := help

include config.mk

CASES := $(notdir $(patsubst %/Makefile,%,$(wildcard cases/[A-Z][0-9][0-9]_*/Makefile)))

.PHONY: help list all clean $(CASES)

help:
	@echo "Usage:"
	@echo "  make list"
	@echo "  make all"
	@echo "  make clean"
	@echo "  make <name>"
	@echo ""
	@echo "Example:"
	@echo "  make A01_case_name"
	@echo ""
	@echo "SLIMMC=$(SLIMMC)"
	@echo "PYTHON=$(PYTHON)"

list:
	@for x in $(CASES); do echo "$$x"; done

all:
	@set -e; for x in $(CASES); do \
		echo "==> $$x"; \
		$(MAKE) -C "cases/$$x" all; \
	done


clean:
	@set -e; for x in $(CASES); do \
		echo "==> CLEAN $$x"; \
		$(MAKE) -C "cases/$$x" clean; \
	done

$(CASES):
	@$(MAKE) -C "cases/$@" all
