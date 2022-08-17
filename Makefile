# Signifies desired executable version
CMD = poetry run python

PACKAGE_DIR = cacha/

.PHONY = help setup test run clean

help:
	@echo "---------------HELP-----------------"
	@echo "Run make _command_. See Makefile for "
	@echo "the reference."
	@echo "------------------------------------"

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

bump-version:
	pip install python-semantic-release==7.31.2
	git config --global user.name "github-actions"
	git config --global user.email "action@github.com"
	python -m semantic-release version -D commit_author="github-actions <action@github.com>"

check-publish:
	poetry config repositories.test-pypi https://test.pypi.org/legacy/
	poetry publish --username ${{ PYPI_USERNAME }} --password ${{ PYPI_TOKEN_TEST }} --dry-run --repository test-pypi

publish:
	poetry publish --username ${{ PYPI_USERNAME }} --password ${{ PYPI_TOKEN_TEST }} --repository test-pypi
