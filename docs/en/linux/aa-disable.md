---
layout: page
title: linux/aa-disable (English)
description: "Disable AppArmor security policy."
content_hash: eb5698025e3b377f7ad1c85758041fd52c39715a
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aa-disable

Disable AppArmor security policy.
See also: `aa-complain`, `aa-enforce`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Disable profile:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>

- Disable profiles:

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profiles</span>
