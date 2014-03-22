from distutils.core import setup, Command
import subprocess


class PyTest(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


setup(name='python-2048a',
      description='A game engine for 2048',
      author='Max Brauer',
      author_email='max@rootswiseyouths.com',
      url='http://github.com/mamachanko/2048',
      packages=['p2048'],
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
