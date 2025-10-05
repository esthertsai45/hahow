.PHONY: format
format:
	isort --atomic --profile black lib tests
	black lib tests

.PHONY: check
check:
	flake8 lib tests --max-line-length 140
	black --check lib tests
	mypy --ignore-missing-imports --check-untyped-defs --no-namespace-packages lib tests