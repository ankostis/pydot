#!/usr/bin/env python
import ast
import codecs
import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


CURRENT_DIR = os.path.dirname(__file__)


def get_long_description():
    readme_path = os.path.join(CURRENT_DIR, "README.md")
    with codecs.open(readme_path, encoding="utf8") as ld_file:
        return ld_file.read()


def get_version():
    pydot_py = os.path.join(CURRENT_DIR, 'pydot.py')
    _version_re = re.compile(r'__version__\s+=\s+(?P<version>.*)')
    with codecs.open(pydot_py, 'r', encoding='utf8') as f:
        match = _version_re.search(f.read())
        version = match.group('version') if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


class PyTest(TestCommand):
    # Allows to pass options to pytest like this:
    # python setup.py test -a "--durations=5"
    user_options = [('pytest-args=', 'a', 'Arguments to pass to pytest')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='pydot',
    version=get_version(),
    description="Python interface to Graphviz's Dot",
    author='Ero Carrera',
    author_email='ero@dkbza.org',
    maintainer='Sebastian Kalinowski',
    maintainer_email='sebastian@kalinowski.eu',
    url='https://github.com/pydot/pydot',
    license='MIT',
    keywords='graphviz dot graphs visualization',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    py_modules=['pydot', 'dot_parser'],
    install_requires=['pyparsing>=2.1.4'],
    tests_require=['pytest', 'chardet', 'mock'],
    cmdclass={'pytest': PyTest},
)
