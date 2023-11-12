---
layout: page
title: freebsd/pkg (English)
description: "FreeBSD package manager."
content_hash: 106dfe04368acbeb093bf5acd6c31a8edd24ab2b
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/freebsd/pkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg

FreeBSD package manager.
More information: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Install a new package:

`pkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Delete a package:

`pkg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages:

`pkg upgrade`

- Search for a package:

`pkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- List installed packages:

`pkg info`

- Remove unneeded dependencies:

`pkg autoremove`
