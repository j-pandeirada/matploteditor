clean: 
	@rm -rf build .local .eggs .pytest_cache dist htmlcov propagator.egg-info .coverage coverage.xml linting.xml report.json report.xml pytest.stdout */__pycache__ */*/__pycache__ || true
.PHONY: clean

lint: clean
	tox -e lint
.PHONY: lint

format: clean
	tox -e format
.PHONY: format

main:
	python3 tests/basic_test.py
.PHONY: main
