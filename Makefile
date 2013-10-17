.PHONY: clean-pyc clean-build docs

help:
	@echo "check - run all checks"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "pep8 - check adherence to PEP8"
	@echo "pyflakes - run pyflakes checks"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

check:
	python setup.py check

clean: clean-build clean-pyc clean-docs

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-docs:
	$(MAKE) -C docs clean

pep8:
	python setup.py pep8

pyflakes:
	python setup.py pyflakes

test:
	python setup.py test

test-all:
	tox

docs:
	rm -f docs/lazarus.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ lazarus
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

release: clean
	python setup.py sdist upload

sdist: clean
	python setup.py sdist
	ls -l dist

