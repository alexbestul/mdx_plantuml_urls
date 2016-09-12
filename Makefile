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

# target: bump_major - Increment the package's major version number, and re-set the minor/patch numbers to 0.
bump_major:
	python ./util/bump_version.py major

# target: bump_minor - Increment the package's minor version number, and re-set the patch number to 0.
bump_minor:
	python ./util/bump_version.py minor

# target:  bump_patch - Increment the package's patch version number.
bump_patch:
	python ./util/bump_version.py patch