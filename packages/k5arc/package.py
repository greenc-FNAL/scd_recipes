# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


def ignore_CVS(path):
    if str(path).find("CVS") >= 0:
        return True
    return False


class K5arc(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://fifewiki.fnal.gov/"
    cvs = ":pserver:anonymous@cdcvs.fnal.gov:/cvs/oss%module=k5arc"
    maintainers("marcmengel")

    version("v1_2")
    version("v1_1")

    def setup_build_environment(self, env):
        env.set("K5ARC_DIR", self.stage.source_path)

    def setup_run_environment(self, env):
        env.set("K5ARC_DIR", self.spec.prefix)

    def install(self, spec, prefix):
        #sh = which("sh")
        #sh("ups/init")
        install_tree(self.stage.source_path, prefix, ignore=ignore_CVS)
