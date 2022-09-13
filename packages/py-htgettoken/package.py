# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os


class PyHtgettoken(PythonPackage):
    """Utility to fetch webtokens from Vault"""

    homepage = "https://github.com/fermitools/htgettoken"
    url = "https://github.com/fermitools/htgettoken/archive/refs/tags/v1.6.tar.gz"

    maintainers = ["mengel", "DrDaveD"]

    version(
        "1.6", sha256="a4e53dec012103fb3fd22389a737fe6bd5bedfda7e639b70b017f5f1a8b69ec3"
    )
    version(
        "1.5", sha256="9c7161eded4369342ee542c1ec7f4c901f478707d424c3c60aebb546e7bfb91f"
    )
    version(
        "1.4", sha256="5d03f644c8e6d5515567cc687b94e135731530b9e4560edabd74d17a62fe213b"
    )

    # depends_on('py-setuptools', type='build')
    depends_on("py-m2crypto", type=("build", "run"))
    depends_on("py-pyopenssl", type=("build", "run"))
    depends_on("py-kerberos", type=("build", "run"))
    depends_on("coreutils", type="run")  # for 'base64'

    def install(self, spec, prefix):
        os.makedirs(prefix.bin)
        os.makedirs(prefix.man)
        filter_file("#!/usr/bin/python3", "#!/usr/bin/env python3", "htgettoken")
        install("htgettoken", prefix.bin)
        install("httokendecode", prefix.bin)
        install("htgettoken.1", prefix.man)

    def build(self, spec, prefix):
        # nothing to build
        pass
