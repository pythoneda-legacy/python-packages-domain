# PythonEDA/python-packages

PythonEDA domain for Python packages.

This package provides:
- [PythonEDAPythonPackages/flit_python_package.py](PythonEDAPythonPackages/flit_python_package.py "FlitPythonPackage"): A Python package using Flit as build system.
- [PythonEDAPythonPackages/pipenv_python_package.py](PythonEDAPythonPackages/pipenv_python_package.py): A Python package using Pipenv. 
- [PythonEDAPythonPackages/poetry_python_package.py](PythonEDAPythonPackages/poetry_python_package.py): A python package using Poetry.
- [PythonEDAPythonPackages/python_package.py](PythonEDAPythonPackages/python_package.py): The representation of a Python package.
- [PythonEDAPythonPackages/python_package_base_event.py](PythonEDAPythonPackages/python_package_base_event.py): Base event for all events in this domain.
- [PythonEDAPythonPackages/python_package_created.py](PythonEDAPythonPackages/python_package_created.py): An event emitted when a Python package is created. 
- [PythonEDAPythonPackages/python_package_factory.py](PythonEDAPythonPackages/python_package_factory.py): A factory of Python packages. 
- [PythonEDAPythonPackages/python_package_in_progress.py](PythonEDAPythonPackages/python_package_in_progress.py): A temporary representation of a Python package not fully created.
- [PythonEDAPythonPackages/python_package_metadata.py](PythonEDAPythonPackages/python_package_metadata.py): Metadata of Python packages. 
- [PythonEDAPythonPackages/python_package_metadata_repo.py](PythonEDAPythonPackages/python_package_metadata_repo.py): Repository of Python package metadata.
- [PythonEDAPythonPackages/python_package_requested.py](PythonEDAPythonPackages/python_package_requested.py): An event emitted when a Python package is requested. 
- [PythonEDAPythonPackages/python_package_resolved.py](PythonEDAPythonPackages/python_package_resolved.py): An event emitted when a Python package is resolved. 
- [PythonEDAPythonPackages/python_package_resolver.py](PythonEDAPythonPackages/python_package_resolver.py): A class responsible of resolving Python packages.
- [PythonEDAPythonPackages/setuppy_python_package.py](PythonEDAPythonPackages/setuppy_python_package.py): A setup.py-based Python package. 
- [PythonEDAPythonPackages/setuptools_python_package.py](PythonEDAPythonPackages/setuptools_python_package.py): A setuptools-based Python package.
- [PythonEDAPythonPackages/unsupported_python_package.py](PythonEDAPythonPackages/unsupported_python_package.py): An error indicating a Python package is not supported.
- [PythonEDAPythonPackages/build/error_creating_a_virtual_environment.py](PythonEDAPythonPackages/build/error_creating_a_virtual_environment.py): An error indicating a virtual environment could not be created.
- [PythonEDAPythonPackages/build/error_installing_setuptools.py](PythonEDAPythonPackages/build/error_installing_setuptools.py): An error installing setuptools.
- [PythonEDAPythonPackages/build/more_than_one_egg_info_folder.py](PythonEDAPythonPackages/build/more_than_one_egg_info_folder.py): An error indicating there're more than one egg_info folder.
- [PythonEDAPythonPackages/build/no_egg_info_folder_found.py](PythonEDAPythonPackages/build/no_egg_info_folder_found.py): An error indicating there's no egg_info folder.
- [PythonEDAPythonPackages/build/pyprojecttoml_utils.py](PythonEDAPythonPackages/build/pyprojecttoml_utils.py): Helper methods for dealing with pyproject.toml files.
- [PythonEDAPythonPackages/build/python_build_resolver.py](PythonEDAPythonPackages/build/python_build_resolver.py): A class responsible for resolving build requests.
- [PythonEDAPythonPackages/build/python_build_strategy_requested.py](PythonEDAPythonPackages/build/python_build_strategy_requested.py): An event requesting which build strategy certain Python package uses.
- [PythonEDAPythonPackages/build/python_setuppy_egg_info_failed.py](PythonEDAPythonPackages/build/python_setuppy_egg_info_failed.py): An error when running `python setup.py egg_info`. 
- [PythonEDAPythonPackages/build/requirementstxt_utils.py](PythonEDAPythonPackages/build/requirementstxt_utils.py): Helper methods for dealing with requirements.txt files.
- [PythonEDAPythonPackages/build/setupcfg_utils.py](PythonEDAPythonPackages/build/setupcfg_utils.py): Helper methods for dealing with setup.cfg files.
- [PythonEDAPythonPackages/build/setuppy_strategy_found.py](PythonEDAPythonPackages/build/setuppy_strategy_found.py): An event emitted when the build strategy for a Python package is known to be setup.py.
