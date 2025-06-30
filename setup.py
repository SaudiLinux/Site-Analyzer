#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="site-analyzer",
    version="1.0.0",
    author="Saudi Crackers",
    author_email="SaudiLinux7@gmail.com",
    description="A comprehensive website analysis and vulnerability scanning tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaudiCrackers/site-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "site-analyzer=site_analyzer:main",
        ],
    },
)