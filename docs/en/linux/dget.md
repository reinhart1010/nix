---
layout: page
title: linux/dget (English)
description: "Download Debian packages."
content_hash: 7d5721e3dfb3de2869988fd95d45b405af2ebe80
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# dget

Download Debian packages.
More information: <https://manned.org/dget.1>.

- Download a binary package:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Download and extract a package source from its `.dsc` file:

`dget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>

- Download a package source tarball from its `.dsc` file but don't extract it:

`dget -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc</span>
