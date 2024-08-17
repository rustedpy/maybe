# phony trick from https://keleshev.com/my-book-writing-setup/
.PHONY: phony

# "True" if running Python < (3, 10); "False" otherwise.
PYTHON_PRE_310 := $(shell python -c "import sys; print(sys.version_info < (3, 10))")

install: phony
	@echo Installing dependencies...
	python -m pip install --require-virtualenv -r requirements-dev.txt
	python -m pip install --require-virtualenv -e .

lint: phony lint-flake lint-mypy

lint-flake:
ifeq ($(PYTHON_PRE_310), True)
	@# Python <3.10 doesn't support pattern matching.
	flake8 --extend-exclude tests/test_pattern_matching.py
else
	flake8
endif

lint-mypy: phony
	mypy

test: phony
	pytest

docs: phony
	lazydocs \
		--overview-file README.md \
		--src-base-url https://github.com/rustedpy/maybe/blob/main/ \
		./src/maybe
