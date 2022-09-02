# Signifies desired executable version
CMD = poetry run python

PACKAGE_DIR = cacha/

.PHONY = help setup test run clean

help:
	@echo "---------------HELP-----------------"
	@echo "Run make _command_. See Makefile for "
	@echo "the reference."
	@echo "------------------------------------"

install-poetry:
	pip install poetry==1.1.14
	
install-prod:
	poetry install --no-dev

install:
	poetry install

test:
	${CMD} -m pytest cacha/tests/

check-all:
	make check-format
	${CMD} -m pylint ${PACKAGE_DIR}
	${CMD} -m mypy --ignore-missing-imports ${PACKAGE_DIR}
	
check-format:
	${CMD} -m black --check ${PACKAGE_DIR}

format:
	${CMD} -m black ${PACKAGE_DIR}

build:
	rm -rf dist
	poetry build

release:
	semantic-release publish

check-publish:
	poetry publish --username ${{ PYPI_USERNAME }} --password ${{ PYPI_TOKEN }} --dry-run 

publish:
	poetry publish --username ${{ PYPI_USERNAME }} --password ${{ PYPI_TOKEN }}
