---
layout: page
title: linux/dget (English)
description: "Download Debian packages."
content_hash: 7d8bba1e6f0e454a5727c19effa5d852ffe13566
last_modified_at: 2023-08-26
---
# dget

Download Debian packages.
More information: <https://manpages.debian.org/latest/devscripts/dget.1.en.html>.

- Download a binary package:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Download and extract a package source from its `.dsc` file:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>

- Download a package source tarball from its `.dsc` file but don't extract it:

`dget -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>
