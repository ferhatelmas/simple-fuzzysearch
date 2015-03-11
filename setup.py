from __future__ import with_statement

try:
    from setuptools import setup
except:
    from distutils.core import setup

import fuzzysearch

fuzzysearch_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.rst", "r") as fp:
    fuzzysearch_long_description = fp.read()

setup(name="simple-fuzzysearch",
      version=fuzzysearch.__version__,
      author="Ferhat Elmas",
      author_email="elmas.ferhat@gmail.com",
      url="https://github.com/ferhatelmas/simple-fuzzysearch",
      py_modules=["fuzzysearch"],
      license="MIT",
      description="Matching a string with partial input",
      long_description=fuzzysearch_long_description,
      classifiers=fuzzysearch_classifiers
      )
