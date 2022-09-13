# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class JobsubLite(Package):
    """HTCondor Job submission wrappers from Fermilab"""

    homepage = "https://github.com/marcmengel/jobsub_lite"
    url = "https://github.com/marcmengel/jobsub_lite/archive/refs/tags/beta12.tar.gz"

    version(
        "beta12",
        sha256="fbdd54966216c3d017f65f255b0f4dc07efe69a0ead1086a375f7e625f3f3cc1",
    )
    version(
        "beta11",
        sha256="76e67503377103ca8b5a5aff7ad4189ebe02ae8e3f8ac5e5bc19bee9d124f428",
    )
    version(
        "beta10",
        sha256="b9cfc4dd93bfb5308ae411982cec26d83480867d9a3ac15dd46c00d1688b8cf0",
    )
    version(
        "beta9",
        sha256="ea7ed67c410283b421f5ec54c76cab86eee2f920f7191530eb8142d545bd8505",
    )

    def url_for_version(self, version):
        url = "https://github.com/marcmengel/jobsub_lite/archive/refs/tags/{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("htcondor", type="run")
    depends_on("cigetcert", type="run")
    depends_on("htgettoken", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
