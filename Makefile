#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = modules
PYTHON_VERSION = 3.9.6
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Create & Activate Python Virtual Environment
.PHONY: createvenv
createvenv:
	$(PYTHON_INTERPRETER) -m venv venv
	source activate venv

## Install Python Dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Run dataset.py
.PHONY: dldata
dldata:
	$(PYTHON_INTERPRETER) modules/dataset.py

## Run tidy.py
.PHONY: prcsdata
prcsdata:
	$(PYTHON_INTERPRETER) modules/tidy.py

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
