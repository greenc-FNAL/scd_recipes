# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Gsoap(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.genivia.com/products.html"
    url      = "https://downloads.sourceforge.net/project/gsoap2/gsoap-2.8/gsoap_2.8.111.zip"

    maintainers = ['marc.mengel@gmail.com', ]

    version('2.8.111', sha256='f1670c7e3aeaa66bc5658539fbd162e5099f022666855ef2b2c2bac07fec4bd3')

    depends_on('openssl')
    depends_on('pkgconfig')

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.prepend_path("PKG_CONFIG_PATH", "%s/lib/ldconfig" % self.prefix)

    def flag_handler(self, name, flags):
        if not name in ['cflags','cxxflags','cppflags']:
            return (flags, None, None)

        flags.append(self.compiler.cc_pic_flag)

        return (None, None, flags)

