#!/usr/bin/env python
import setuptools
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "qthvym",
    version = "0.13",
    author = "Fibo Metavinci",
    author_email = "pszdw-75nat-5227i-bha5s-y7lai-pebdq-o2agp-3xho4-hd6z6-emxrd-nqe@dmail.ai",
    description = "QT UI for HVYM.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/inviti8",
    project_urls = {
        "Bug Tracker": "https://github.com/inviti8/QtHVYM/issues",
    },
    package_dir = {"": "qthvym"},
    packages = setuptools.find_packages(where="qthvym"),
    include_package_data=True, 
    python_requires = ">=3.9.18"
)