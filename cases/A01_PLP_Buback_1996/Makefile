include ../../config.mk

MODEL := A01_PLP_Buback_1996.model

.PHONY: all check run analyze clean

all: check run analyze

check:
	$(SLIMMC) --check $(MODEL)

run:
	$(SLIMMC) $(MODEL)

analyze:
	$(PYTHON) analyze.py

clean:
	rm -rf results figures slurm_logs
