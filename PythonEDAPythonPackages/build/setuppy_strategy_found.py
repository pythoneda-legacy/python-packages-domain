from PythonEDA.value_object import attribute
from PythonEDAPythonPackages.python_package import PythonPackage
from PythonEDAPythonPackages.python_package_base_event import PythonPackageBaseEvent


class SetuppyStrategyFound(PythonPackageBaseEvent):
    """
    Represents the event triggered when a Python package can be built using setup.py.
    """

    def __init__(self, pythonPackage: PythonPackage):
        """Creates a new PythonBuildStrategyRequested instance"""
        super().__init__(pythonPackage.name, pythonPackage.version, pythonPackage.git_repo)
        self._pythonPackage = pythonPackage

    @property
    @attribute
    def pythonPackage() -> PythonPackage:
        return self._pythonPackage
