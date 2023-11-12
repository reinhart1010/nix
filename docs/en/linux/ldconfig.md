---
layout: page
title: linux/ldconfig (English)
description: "Configure symlinks and cache for shared library dependencies."
content_hash: 79b3ff76b2451c6464b25301a1aa06e91086523c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ldconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ldconfig

Configure symlinks and cache for shared library dependencies.
More information: <https://manned.org/ldconfig>.

- Update symlinks and rebuild the cache (usually run when a new library is installed):

`sudo ldconfig`

- Update the symlinks for a given directory:

`sudo ldconfig -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Print the libraries in the cache and check whether a given library is present:

`ldconfig -p | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_name</span>
