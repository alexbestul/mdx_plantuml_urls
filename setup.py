import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

# Helper class for binding the 'setup.py test' command to pytest.
# Taken from the pytest docs:  http://doc.pytest.org/en/latest/goodpractices.html#manual-integration
class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='mdx_plantuml_urls',
    version='0.1',
    setup_requires=['plantuml', 'markdown'],
    tests_require=['pytest', 'mock', 'pytest-mock'],
    test_suite = "not None",  # Without it, run_tests is not called.
    cmdclass = {'test': PyTest},
    author = 'alexbestul',
    author_email = 'alexbestul@users.noreply.github.com',
    url = 'https://github.com/alexbestul/mdx_plantuml_urls'
)
