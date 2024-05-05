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

publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
