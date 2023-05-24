#!/usr/bin/env python3
from pythoneda.application.pythoneda import PythonEDA

import asyncio

class EcosystemPythonPackages(PythonEDA):

    def __init__(self):
        super().__init__()

if __name__ == "__main__":

    asyncio.run(EcosystemPythonPackages.main())
