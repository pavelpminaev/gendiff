install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest