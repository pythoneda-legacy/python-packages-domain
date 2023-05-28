from distutils.core import setup
setup(
    name = "pythoneda-python-packages",
    packages = ["EDAPythonPackages"],
#    packages = find_packages(),
    version = "0.0.1a1",
    description = "Python packages in PythonEDA",
    author = "rydnr",
    author_email = "github@acm-sl.org",
    url = "https://github.com/rydnr/pythoneda-python-packages",
    download_url = "https://github.com/rydnr/pythoneda-python-packages/releases",
    keywords = ["eda", "ddd"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires=[
    ],
    long_description = """\
Python packages in PythonEDA
----------------------------

This package includes the domain of Python packages in PythonEDA.

This is what PythonEDA Python Packages provides:
- EDAPythonPackages/python_package: An abstraction of Python packages.
- EDAPythonPackages/flit_python_package: Python packages using Flit as build mechanism.
- EDAPythonPackages/pipenv_python_package: Python packages using Pipenv.
- EDAPythonPackages/poetry_python_package: Python packages using Poetry.
- EDAPythonPackages/setuppy_python_package: Python packages using Setup.py.
- EDAPythonPackages/setuptools_python_package: Python packages using Setuptools.
- EDAPythonPackages/python_package_metadata: Metadata for a Python package.
- EDAPythonPackages/python_package_metadata_repo: Repository to access the metadata for a Python package.
- EDAPythonPackages/*: Events involved in Python packages lifecycle.
- EDAPythonPackages/build/python_build_resolver: A class to resolve how to build Python packages.
- EDAPythonPackages/build/*_utils: Utility classes.
- EDAPythonPackages/build/*: Events and errors involved in building Python packages.
""",
    tests_require=['pytest']
)
