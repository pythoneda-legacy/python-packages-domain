from EDAPythonPackages.python_package import PythonPackage
from EDAPythonPackages.python_package_base_event import PythonPackageBaseEvent
from PythonEDA.value_object import primary_key

class PythonPackageCreated(PythonPackageBaseEvent):
    """
    Represents the event when a PythonPackage has been created.
    """

    def __init__(self, package: PythonPackage):
        """Creates a new PythonPackageCreated instance"""
        self._package = package

    @property
    @primary_key
    def package(self):
        return self._package
