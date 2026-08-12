include ../../config.mk

MODEL := case.model

.PHONY: all check run analyze clean

all: check run analyze

check:
	$(SLIMMC) --check $(MODEL)

run:
	$(SLIMMC) $(MODEL)

analyze:
	$(PYTHON) analyze.py

clean:
	rm -rf results figures
