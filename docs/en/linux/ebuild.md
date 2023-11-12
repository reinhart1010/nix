---
layout: page
title: linux/ebuild (English)
description: "A low level interface to the Gentoo Portage system."
content_hash: 5130b7b01d25da339a3a18f7ae653d84d01cd30d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ebuild

A low level interface to the Gentoo Portage system.
More information: <https://wiki.gentoo.org/wiki/Ebuild>.

- Create or update the package manifest:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` manifest`

- Clean the temporary build directories for the build file:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` clean`

- Fetch sources if they do not exist:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` fetch`

- Extract the sources to a temporary build directory:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` unpack`

- Compile the extracted sources:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` compile`

- Install the package to a temporary install directory:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` install`

- Install the temporary files to the live filesystem:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` qmerge`

- Fetch, unpack, compile, install and qmerge the specified ebuild file:

`ebuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ebuild</span>` merge`
