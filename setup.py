"""Setuptools install script for pytest-timeout."""
from setuptools import setup

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="pytest-timeout-pass",
    description="pytest plugin to kill long-running tests after startup phase and mark them as passed",
    long_description=long_description,
    version="0.1.0",
    author="Thomas G. Close",
    author_email="tom.g.close@gmail.com",
    url="https://github.com/tclose/pytest-timeout-pass",
    license="MIT",
    py_modules=["pytest_timeout_pass"],
    entry_points={"pytest11": ["timeout_pass = pytest_timeout_pass"]},
    install_requires=["pytest>=5.0.0"],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: DFSG approved",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
        "Framework :: Pytest",
    ],
)
