from spack import *


class SpackInfrastructure(Package):
    """Spack utility scripts, etc"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/spack-infrastrucutre"
    url = "https://github.com/FNALssi/spack-infrastructure/archive/refs/tags/v2.19.0.tar.gz"

    version("2.19.0", sha256="274aafb4ffad82205c8972c6aa85c04e5fdc86ce856c7701105b3b7a13159763")
    version("2_18_00_01", sha256="52d60684a359060ef95c91b9fb4adf0d114b28437144dc496118ccf39af89fd0")
    version("master", git="https://github.com/FNALssi/spack-infrastructure/")

    def url_for_version(self, version):
        fmt="https://github.com/FNALssi/spack-infrastructure/archive/refs/tags/v{0}.tar.gz"
        return fmt.format(version)

    depends_on("python", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
