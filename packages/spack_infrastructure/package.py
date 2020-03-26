from spack import *

class SpackInfrastructure(Package):
    """Production Operations Management System"""

    homepage = "http://cdcvs.fnal.gov/redmine/projects/spack-infrastrucutre"
    url = 'http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/spack-infrastructure.v1_2.tar'

    version('1_3', sha256='8a00ee68d66f072987f164763545ce88e1f885e1475e2a77423133ae24e8ae16')
    version('1_2', sha256='8bab9965072f8ef4933e166fafb9a4c6cf14cbcdc8550b314a76d23bce926aa7')

    depends_on('python',               type=('build','run'))

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
