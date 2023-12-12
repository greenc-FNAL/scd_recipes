# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class DataDispatcher(PythonPackage):
    """Data Dispatcher for processing large filesets"""

    homepage = "https://github.com/ivmfnal/data_dispatcher"
    pypi = "datadispatcher/datadispatcher-1.15.2.tar.gz"
    git = "https://github.com/ivmfnal/data_dispatcher.git"

    maintainers("marcmengel", "ivmfnal")

    version("1.26.0", sha256="c4492b7b2f20761c8f4e4e8f746088b75ff953f49ec3c179bab42064778d2edf")
    version("1.25.0", sha256="2cc09dbc3922dd0a4c8af1e7d05084f6dfea29594bfc4b39b43c91e7df256adf")
    version("1.24.3", sha256="bed5898beed536eaf6e975a14f9b03e1294196bee7bd7e979d5edee39b466292")
    version("1.24.0", sha256="05cd15ff9084fd7a937536c040180624cacec5806294a3103f756152aac1bb7b")
    version("1.19.0", sha256="5447ee6ee15686144844e5dd0eb12c0bbb64677491021d73a59665b426b8a648")

    version("1.15.2", sha256="a086c9835558e3c43a45c3eacc3879b5062da58bbdc7db8222ad576e3c190c1c")
    version("1.15.1", sha256="b8ccc107b4b10a1a9253d1859e6fcef69b05bddf8e598977ea0078cdf4798ed7")
    version("1.15.0", sha256="aede4a3ec1a3ee79f8bd38448fd485e513ca303414d3f96cff74b72ae3c763e5")
    version("main", branch="main")

    # the 3.7 versioning actually comes from the metacat docs... 
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-requests", type=("build", "run"))
    depends_on("metacat@3.9.3:", type=("build", "run"))

    @run_after("install")
    def remove_extra_name(self):
        # data-dispatcher installs identicaly "ddint" and "dd", but the
        # latter obscures /bin/dd and breaks ifdhc...
        os.unlink(self.spec.prefix.bin.dd)
