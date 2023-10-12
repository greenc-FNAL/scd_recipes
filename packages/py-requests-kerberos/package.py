# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyRequestsKerberos(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/requests/requests-kerberos"
    pypi = "requests-kerberos/requests-kerberos-0.14.0.tar.gz"

    maintainers = ["marcmengel",]

    version("0.14.0", sha256="cda9d1240ae5392e081869881c8742d0e171fd6a893a7ac0875db2748e966fd1")

    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pyspnego", type=("build", "run"))
    depends_on("py-cryptography", type=("build", "run"))
