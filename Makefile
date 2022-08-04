# Signifies desired executable version
CMD = poetry run python

PACKAGE_DIR = cache_manager/

.PHONY = help setup test run clean

help:
	@echo "---------------HELP-----------------"
	@echo "Run make _command_. See Makefile for "
	@echo "the reference."
	@echo "------------------------------------"

install:
	poetry install

test:
	${CMD} -m pytest cache_manager/tests/

check-all:
	make check-format
	${CMD} -m pylint ${PACKAGE_DIR}
	${CMD} -m mypy ${PACKAGE_DIR}
	
check-format:
	${CMD} -m black --check ${PACKAGE_DIR}

format:
	${CMD} -m black ${PACKAGE_DIR}

build:
	rm -rf dist
	poetry build

publish:
	poetry publish