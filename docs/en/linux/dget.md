---
layout: page
title: linux/dget (English)
description: "Download Debian packages."
content_hash: cae40bb273953a5a1d3e80e501c31be690186375
---
# dget

Download Debian packages.
More information: <https://manpages.debian.org/dget>.

- Download a binary package:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Download and extract a package source from its `.dsc` file:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>

- Download a package source tarball from its `.dsc` file but don't extract it:

`dget -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>
