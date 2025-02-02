# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIpcRun3(PerlPackage):
    """Run a subprocess with input/ouput redirection"""

    homepage = "https://metacpan.org/pod/IPC::Run3"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-0.048.tar.gz"

    maintainers("EbiArnie")

    version("0.048", sha256="3d81c3cc1b5cff69cca9361e2c6e38df0352251ae7b41e2ff3febc850e463565")

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use IPC::Run3; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
