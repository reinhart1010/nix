---
layout: page
title: linux/gbp (English)
description: "A system to integrate the Debian package build system with Git."
content_hash: dbf3f371a9046a43b7a19cd75b3c0631fc9319d8
---
# gbp

A system to integrate the Debian package build system with Git.
More information: <http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- Convert an existing Debian package to gbp:

`gbp import-dsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.dsc</span>

- Build the package in the current directory using the default builder (`debuild`):

`gbp buildpackage -jauto -us -uc`

- Build a package in a `pbuilder` environment for Debian Bullseye:

`DIST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bullseye</span>` ARCH=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amd64</span>` gbp buildpackage -jauto -us -uc --git-builder=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git-pbuilder</span>

- Specify a package to be a source-only upload in the `.changes` file (see https://wiki.debian.org/SourceOnlyUpload):

`gbp buildpackage -jauto -us -uc --changes-options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S</span>

- Import a new upstream release:

`gbp import-orig --pristine-tar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.tar.gz</span>
