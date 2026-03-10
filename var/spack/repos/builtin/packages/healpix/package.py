# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Healpix(AutotoolsPackage):
    """Healpix is a C/C++ library for calculating
    Hierarchical Equal Area isoLatitude Pixelation of a sphere."""

    homepage = "https://healpix.sourceforge.io"

    version("3.82.0", sha256="47629f057a2daf06fca3305db1c6950edb9e61bbe2d7ed4d98ff05809da2a127", url="https://sourceforge.net/projects/healpix/files/Healpix_3.82/Healpix_3.82_2022Jul28.tar.gz/download")

    depends_on("cfitsio")
    depends_on("libsharp2")
