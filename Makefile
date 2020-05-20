.PHONY: test upload clean bootstrap venv lint dev build

TEST_PATH := ./

format:
	@black .

test:
	@python3 -m pytest --verbose $(TEST_PATH)

venv:
	@virtualenv venv

clean:
	@rm -rf build/
	@rm -rf dist/
	@rm -Rf *.egg-info 

bootstrap:
	venv/bin/pip3 install -e .

dev:
	@pip3 install -r requirements.txt
	@pip3 install -r requirements.dev.txt

build:
	@python3 setup.py sdist bdist_wheel

upload:
	@twine upload dist/*