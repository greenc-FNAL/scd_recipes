# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class PyGfal2Util(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://dmc.web.cern.ch/"
    url      = "https://gitlab.cern.ch/dmc/gfal2-bindings/-/archive/v1.8.3/gfal2-util-v1.5.3.tar.gz"

    maintainers = ['marcmengel',]

    version('1.5.3', sha256='803ed5dbcff8a59fe4fec30ab825535c28fa895b61b1ce5d36d850e80fc5b24a')

    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('gfal2-python',        type=('build', 'run'))

