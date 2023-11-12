---
layout: page
title: linux/dpkg-query (English)
description: "A tool that shows information about installed packages."
content_hash: a3a33b1c46f674bb9a888b0b332194bfef43a395
last_modified_at: 2023-11-12
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

A tool that shows information about installed packages.
More information: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

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
