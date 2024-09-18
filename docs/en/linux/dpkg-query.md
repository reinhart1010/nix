---
layout: page
title: linux/dpkg-query (English)
description: "Display information about installed packages."
content_hash: 839522585b2bd4a49884b7b71f63c3b649ab4d78
last_modified_at: 2024-09-18
related_topics:
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-query

Display information about installed packages.
More information: <https://manned.org/dpkg-query.1>.

- List all installed packages:

`dpkg-query --list`

- List installed packages matching a pattern:

`dpkg-query --list '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6*</span>`'`

- List all files installed by a package:

`dpkg-query --listfiles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Show information about a package:

`dpkg-query --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Search for packages that own files matching a pattern:

`dpkg-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/ld.so.conf.d</span>
