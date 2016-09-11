# target: help - Display callable targets.
help:
	@grep --color=never "^# target:" [Mm]akefile

# target: test - Run all tests.
test:
	python setup.py test

# target: clean - Clean up temporary files, artifacts, etc.
clean:
	@rm -r -f *.egg/
	@rm -r -f *.egg-info/
	@rm -r -f wheelhouse/
	@rm -r -f tests/__pycache__/
	@rm -r -f .eggs/
	@rm -r -f .cache/
	@rm -r -f *.pyc