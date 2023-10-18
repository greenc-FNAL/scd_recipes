# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class RmdConfig(BundlePackage):
    """Config for rucio-clients, metacat and data-dispatcher"""

    homepage = "https://fifewiki.fnal.gov/"

    maintainers("marcmengel")

    version("1.0")

    depends_on("data-dispatcher")
    depends_on("rucio-clients")
    depends_on("metacat")

    variant("experiment", 
        values=[
            "hypot",
            "annie",
            "dune",
            "gm2",
            "icarus",
            "lariat",
            "minerva",
            "mu2e",
            "nova",
            "sbn",
            "sbnd",
            "uboone",
        ],
        default="hypot"
    )
    
    variant("lab", values= ["fnal.gov"], default="fnal.gov")

    def get_rdict(self):
        rdict = { 
            "exp": self.spec.variants["experiment"].value,
            "lab": self.spec.variants["lab"].value,
            "msuf": "_meta_prod/app",
            "dsuf": "_dd_prod/data",
            "asuf": ""
        }
        # irregularities...
        if rdict["exp"] == "hypot":
            rdict["msuf"] = "_meta_dev/app"
            rdict["dsuf"] = "_dd/data"
            rdict["asuf"] = "_dev"
        if rdict["exp"] == "dune":
            rdict["msuf"] = "_meta_demo/app"
            rdict["dsuf"] = "/dd/app"
        
        return rdict


    def setup_run_environment(self, env):
        rdict = self.get_rdict()
        ddurl = "https://metacat.%(lab)s:9443/%(exp)s%(dsuf)s" % rdict
        msurl = "https://metacat.%(lab)s:9443/%(exp)s%(msuf)s" % rdict
        authurl = "https://metacat.%(lab)s:8143/auth/%(exp)s%(asuf)s" % rdict
        if rdict["exp"] == "mu2e":
            msurl = msurl.replace("metacat", "dbweb5")
        env.set( "RUCIO_HOME", self.spec.prefix )
        env.set( "DATA_DISPATCHER_URL", ddurl )
        env.set( "METACAT_SERVER_URL", msurl )
        env.set( "DATA_DISPATCHER_AUTH_URL", authurl)
        env.set( "METACAT_AUTH_SERVER_URL", authurl)

    def install(self, spec, prefix):
        edir = str(prefix.etc)
        rdict = self.get_rdict()
        makedirs(edir)
        with open( os.path.join(edir, "rucio.cfg"), "w") as rcf:
            rcf.write("""
[client]
rucio_host = https://%(exp)s-rucio.%(lab)s
auth_host = https://auth-%(exp)s-rucio.%(lab)s

ca_cert = /etc/grid-security/certificates
account = ${USER}
auth_type = x509_proxy
#client_x509_proxy = $X509_USER_PROXY
request_retries = 3
"""     % rdict)

