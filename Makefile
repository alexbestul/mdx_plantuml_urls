# target: help - Display callable targets.
help:
	@grep --color=never "^# target:" [Mm]akefile

# target: test - Run all tests.
test:
	python setup.py test