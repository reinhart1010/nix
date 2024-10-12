---
layout: page
title: linux/checkinstall (English)
description: "Track the local installation of a software package, and produce a binary package which can be used with a system's native package manager."
content_hash: 6545831194dd9e7c0d445b068c7ab0206c867cca
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# checkinstall

Track the local installation of a software package, and produce a binary package which can be used with a system's native package manager.
More information: <https://checkinstall.izto.org>.

- Create and install a package with default settings:

`sudo checkinstall --default`

- Create a package but don't install it:

`sudo checkinstall --install=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>

- Create a package without documentation:

`sudo checkinstall --nodoc`

- Create a package and set the name:

`sudo checkinstall --pkgname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Create a package and specify where to save it:

`sudo checkinstall --pakdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
