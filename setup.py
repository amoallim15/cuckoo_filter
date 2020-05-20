import sys
import os
from setuptools import find_packages, setup

_locals = {}
exec(open("cuckoo_filter/_version.py").read(), None, _locals)
version = _locals["__version__"]
install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("requirements.dev.txt").read().strip("\n")
long_description = open("README.md").read()

setup(
    name="cuckoo_filter",
    version=version,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    python_requires=">=3.6",
    description="Cuckoo Filter: Practically Better Than Bloom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amoallim15/Cuckoo-Filter",
    license="MIT License",
    author="Ali Moallim",
    author_email="amoallim15@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
