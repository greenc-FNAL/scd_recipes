# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlGraphviz2(PerlPackage):
    """A wrapper for AT&T's Graphviz"""

    homepage = "https://metacpan.org/pod/GraphViz2"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETJ/GraphViz2-2.67.tar.gz"

    maintainers("marcmengel")

    version("2.67", sha256="87c85c6edffcea4f96e6b4800f6f9512aeab19eb8d3b348301a721331bcb8580")
    version("2.66", sha256="049d8a7d3b3bcbe30d9e05fb53afe8b10c6a8f122571394e9e087c725362e69c")
    version("2.65", sha256="c87776faa065fe86f7ac3147f9e13075c87e6771b2972ca8b84c04fe28516f81")
    version("2.64", sha256="f946bfd4141d3ca80fe2baca627a3f1cfee4fcd61c39992e608be31a834b73cd")

    depends_on("perl-moo", type=("build", "run"))
    depends_on("perl-file-which", type=("build", "run"))
    depends_on("perl-graph", type=("build", "run"))
    depends_on("perl-data-section-simple", type=("build", "run"))
    depends_on("perl-ipc-run3", type=("build", "run"))

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
