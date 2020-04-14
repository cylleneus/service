#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

version = "0.0.2"

requirements = ["cylleneus>=0.3.4", "celery[redis]>=4.4.0", "fastapi>=0.46.0", "rabbitmq>=0.2.0", "uvicorn>=0.11.1"]

setup_requirements = []

test_requirements = []

setup(
    author="William Michael Short",
    author_email="w.short@exeter.ac.uk",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Next-generation search engine for electronic corpora of ancient languages",
    entry_points={"console_scripts": ["cylleneus-service=service.server:run", ], },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="cylleneus",
    name="cylleneus-service",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/cylleneus/service",
    version=version,
    zip_safe=False,
)
