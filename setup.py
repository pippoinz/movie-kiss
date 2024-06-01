"""
This module contains the setup script for the movie-kiss project.

The movie-kiss project is a Python project based on clean architecture for movie selection.

Author: Alexandre Leroux
Email: alex.leroux89@gmail.com
"""

from setuptools import setup, find_packages

setup(
    name="movie-kiss",
    version="0.1.0",
    description="A Python project based on clean architecture for movie selection",
    author="Alexandre Leroux",
    author_email="alex.leroux89@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
