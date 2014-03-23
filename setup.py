from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name='python-2048a',
      description='A game engine for 2048',
      author='Max Brauer',
      author_email='max@rootswiseyouths.com',
      url='http://github.com/mamachanko/2048',
      packages=find_packages(),
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Topic :: Games/Entertainment :: Board Games",
          "Intended Audience :: Developers",
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"])
