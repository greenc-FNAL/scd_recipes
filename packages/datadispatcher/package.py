# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Datadispatcher(PythonPackage):
    """Data Dispatcher for processing large filesets"""

    homepage = "https://github.com/ivmfnal/data_dispatcher"
    pypi = "datadispatcher/datadispatcher-1.15.2.tar.gz"

    maintainers = ["marcmengel", "ivmfnal"]

    version("1.15.2", sha256="a086c9835558e3c43a45c3eacc3879b5062da58bbdc7db8222ad576e3c190c1c")
    version("1.15.1", sha256="b8ccc107b4b10a1a9253d1859e6fcef69b05bddf8e598977ea0078cdf4798ed7")
    version("1.15.0", sha256="aede4a3ec1a3ee79f8bd38448fd485e513ca303414d3f96cff74b72ae3c763e5")

    # the 3.7 versioning actually comes from the metacat docs... 
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-metacat@3.9.3:", type=("build", "run"))
