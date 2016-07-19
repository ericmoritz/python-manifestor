test: deps
	py.test --doctest-modules --pep8 bin/ manifestor/ features/steps

integration: test
	behave

deps:
	pip install -e .
