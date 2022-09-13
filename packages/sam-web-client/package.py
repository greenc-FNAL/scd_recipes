# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class SamWebClient (Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sam-web-client/wiki"
    url      = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-web-client.v3_0.tar"


    version('2.0', sha256='9a2729e01a0e143f8d30fdd17a40038e088a86931b14950dcb370746af7e9cba')
    version('2.1', sha256='d2e875b44ea25fa3a681f24e15d6f525c3be3c9ccc54e162981814dbccaf801a')
    version('3.0', sha256='e03a4c9e34175ccc899cc3fc149022423ba45b60c09fbac6db3f1184d974f0ff')

    #version('3.1')

    def url_for_version(self, version):
        url = 'https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-web-client.v{0}.tbz2'
        return url.format(version.underscored)


    depends_on('python', type=('build','run'))
    depends_on('py-requests',type='run')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.prefix.bin)
        run_env.prepend_path('PYTHONPATH', self.prefix + '/python')

