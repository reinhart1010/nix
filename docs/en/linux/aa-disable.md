---
layout: page
title: linux/aa-disable (English)
description: "Disable AppArmor security policies."
content_hash: ea654d7042c05b09ac86f10d4f4bcdd262bfb119
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# aa-disable

Disable AppArmor security policies.
See also: `aa-complain`, `aa-enforce`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Disable profile:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile1 path/to/profile2 ...</span>

- Disable profiles (defaults to `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profiles</span>
