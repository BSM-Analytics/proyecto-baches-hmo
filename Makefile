#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = modules
PYTHON_VERSION = 3.9.6
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Create Python Virtual Environment
.PHONY: create_venv
create_venv:
	$(PYTHON_INTERPRETER) -m venv venv

## Activate Python Virtual Environment
.PHONY: activate_venv
activate_venv:
	(source venv/bin/activate;)

## Install venv Python Dependencies
.PHONY: install_venv_requirements
install_venv_requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Run dataset.py
.PHONY: download_data
download_data:
	$(PYTHON_INTERPRETER) modules/dataset.py

## Run tidy.py
.PHONY: tidy_data
tidy_data:
	$(PYTHON_INTERPRETER) modules/tidying.py

## Run full pipeline
.PHONY: execute_full_pipeline
execute_full_pipeline:
	$(PYTHON_INTERPRETER) -m venv venv
	(source venv/bin/activate;)
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	$(PYTHON_INTERPRETER) modules/dataset.py
	$(PYTHON_INTERPRETER) modules/tidying.py

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
