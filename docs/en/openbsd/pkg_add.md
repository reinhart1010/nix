---
layout: page
title: openbsd/pkg_add (English)
description: "Install/update packages in OpenBSD."
content_hash: 277f444a4036e0d64561cd4d0843bbfa8f1f7f30
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_add

Install/update packages in OpenBSD.
See also: `pkg_info`, `pkg_delete`.
More information: <https://man.openbsd.org/pkg_add>.

- Update all packages, including dependencies:

`pkg_add -u`

- Install a new package:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install packages from the raw output of `pkg_info`:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
