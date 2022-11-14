# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Metacat(PythonPackage):
    """"""

    homepage = "https://metacat.readthedocs.io/en/latest/index.html"
    pypi = "metacat/metacat-3.20.0.tar.gz"

    maintainers = ["marcmengel", "ivmfnal"]

    version("3.20.0", sha256="4f981b755bb914c503db9480b4dab19093a3f5680622c5d9b1913deb17b7ed12")
    version("3.19.1", sha256="c7473233a80926905ec310dfb78a5d61cb52fec9e3f2e154fed577a020573512")
    version("3.19.0", sha256="6366f1379eb9946e7ff29d972b3abb253a59f7e183f43fb598e1ae6ded6b1424")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with when("@3.20.1:"):
        variant("client_only", default=True)

    with when("@:3.20.0"):
        variant("client_only", default=False)

    depends_on("py-pyjwt", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pythreader@2.8.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"), when="~client_only")
    depends_on("py-lark", type=("build", "run"), when="~client_only")

    #@run_before("install")
    #def use_setup_full(self):
    #    with when("~client_only @3.20.1:"):
    #        rename("setup.py","setup_client_only.py")
    #        rename("setup_full.py", "setup.py")

