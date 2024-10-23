---
layout: page
title: linux/aa-disable (English)
description: "Disable AppArmor security policies."
content_hash: 5b137005b5c4bfb8d71243352d279df93c9547d1
last_modified_at: 2024-10-23
related_topics:
  - title: español version
    url: /es/linux/aa-disable.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

Disable AppArmor security policies.
See also: `aa-complain`, `aa-enforce`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Disable profile:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile1 path/to/profile2 ...</span>

- Disable profiles in a directory (defaults to `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profiles</span>
