# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install k-callgraph
#
# You can edit this file again by typing:
#
#     spack edit k-callgraph
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class KCallgraph(Package):
    """Generate static call graphs for multiple languages"""

    homepage = "https://github.com/koknat/callGraph"
    url = "https://github.com/koknat/callGraph/archive/fc9973063e2094d606902e9614e8e7901fe7d392.zip"
    maintainers("marcmengel")

    version("fc997306", url="https://github.com/koknat/callGraph/archive/fc9973063e2094d606902e9614e8e7901fe7d392.zip", md5="8e4bd5683cfb6872f5da9c7c746edc32")

    depends_on("perl-graphviz2")

    def install(self, spec, prefix):
        makedirs(prefix.bin)
        copy("callGraph", prefix.bin)
