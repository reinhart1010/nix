---
layout: page
title: openbsd/pkg_delete (English)
description: "Remove packages in OpenBSD."
content_hash: 95061a6bfe15b8d1ab97224b3eb9bdd4743dcb98
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_delete

Remove packages in OpenBSD.
See also: `pkg_add`, `pkg_info`.
More information: <https://man.openbsd.org/pkg_delete>.

- Delete a package:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Delete a package, including its unused dependencies:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Dry-run deletion of a package:

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
