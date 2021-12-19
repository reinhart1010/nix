---
layout: page
title: linux/dpkg-query (English)
description: "A tool that shows information about installed packages."
content_hash: ca1ad5f5fc40495cb9ec47deb32c5e1d8f7cd898
related_topics:
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg-query.html
    icon: bi bi-globe
---
# dpkg-query

A tool that shows information about installed packages.
More information: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- List all installed packages:

`dpkg-query -l`

- List installed packages matching a pattern:

`dpkg-query -l '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`'`

- List all files installed by a package:

`dpkg-query -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Show information about a package:

`dpkg-query -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
