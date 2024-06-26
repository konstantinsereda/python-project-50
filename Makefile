install:
	poetry install

gendiff:
	poetry run gendiff


lint:
	poetry run flake8 gendiff


build:
	rm -f dist/*
	poetry version --next-phase 0.1.0
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
