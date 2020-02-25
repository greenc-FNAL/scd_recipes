# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class SamWebClient (Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sam-web-client/wiki"
    url      = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-web-client.v3_0.tar"

    version('2.1')
    version('2.2')
    version('3.0')
    #version('3.1')

    depends_on('python', type=('build','run'))
    depends_on('py-requests',type='run')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.prefix.bin)
        run_env.prepend_path('PYTHONPATH', self.prefix + '/python')

