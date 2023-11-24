# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PomsJobsubWrapper(Package):
    """python / command line package for POMS clients"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/poms-client/wiki"
    url = "https://github.com/fermitools/poms/archive/refs/tags/v4_4_2.tar.gz"

    version("4.5.0", sha256="3207db3f1faf628a2a10d078d77334258eca549345439702d6ca103d369d20dd")

    def url_for_version(self, version):
        url = "https://github.com/fermitools/poms/archive/refs/tags/wrapper_v{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path+"/poms_jobsub_wrapper", prefix)

    def setup_environment(self, spack_env, run_env):
        env.prepend_path("JOBSUB_EXTRA_JOB_INFO", "{0}/bin/poms_job_info".format(self.spec.prefix))

        env.prepend_path("JOBSUB_EXTRA_LINES", "+FIFE_CATEGORIES='POMS_TASK_ID_{0};POMS_CAMPAIGN_ID_{1};{0}'".format(
           os.environ["POMS_TASK_ID"], os.environ["POMS_CAMPAIGN_ID"], os.environ["POMS_CAMPAIGN_TAGS"] 
        ))
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_TASK_ID={0}".format(os.environ["POMS_TASK_ID"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_CAMPAIGN_ID={0}".format(os.environ["POMS_CAMPAIGN_ID"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_LAUNCHER={0}".format(os.environ["POMS_LAUNCHER"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_CAMPAIGN_NAME='{0}'".format(os.environ.get["POMS_CAMPAIGN_NAME"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_STAGE_ID={0}".format(os.environ["POMS4_CAMPAIGN_STAGE_ID"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_STAGE_NAME='{0}'".format(os.environ["POMS4_CAMPAIGN_STAGE_NAME"]), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_ID={0}".format(os.environ["POMS4_CAMPAIGN_ID"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_NAME='{0}'".format(os.environ["POMS4_CAMPAIGN_NAME"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_SUBMISSION_ID={0}".format(os.environ["POMS4_SUBMISSION_ID"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_TYPE='{0}'".format(os.environ["POMS4_CAMPAIGN_TYPE"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_TEST_LAUNCH={0}".format(os.environ["POMS4_TEST_LAUNCH"] ), ",")
        env.prepend_path("JOBSUB_EXTRA_ENVIRONMENT", "POMS_CAMPAIGN_ID", ",")
        env.prepend_path("JOBSUB_EXTRA_ENVIRONMENT", "POMS_TASK_ID", ",")

