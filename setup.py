#!/usr/bin/env python

from setuptools import setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "blspy>=0.9",
]

dev_dependencies = [
    "alvm_tools>=0.4.2",
    "pytest",
]

setup(
    name="alvm",
    version='0.9.6',
    packages=["alvm",],
    author="Sten Achiho",
    author_email="sten@achicoin.org",
    url="https://github.com/Achi-Coin/alvm",
    license="https://opensource.org/licenses/Apache-2.0",
    description="[Achi Language | Achilang] Virtual Machine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=dependencies,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(dev=dev_dependencies,),
    project_urls={
        "Bug Reports": "https://github.com/Achi-Coin/alvm",
        "Source": "https://github.com/Achi-Coin/alvm",
    },
)
