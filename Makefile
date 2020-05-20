.PHONY: test upload clean bootstrap env

TEST_PATH := ./

lint:
	black .
	flake8

test:
	@python3 -m pytest --verbose $(TEST_PATH)

venv:
	@virtualenv venv

clean:
	@rm --force --recursive build/
	@rm --force --recursive dist/
	@rm --force --recursive *.egg-info

bootstrap:
	venv/bin/pip3 install -e .

dev:
	@pip3 install -r requirements.txt
	@pip3 install -r requirements.dev.txt

build:
	@python3 setup.py sdist

upload:
	@twine upload dist/*