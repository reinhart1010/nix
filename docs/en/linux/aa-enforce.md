---
layout: page
title: linux/aa-enforce (English)
description: "Set an AppArmor profile to enforce mode."
content_hash: c5e96d68428c6821a881bec95d839c79a21d140a
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aa-enforce

Set an AppArmor profile to enforce mode.
See also: `aa-complain`, `aa-disable`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Enable profile:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>

- Enable profiles:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>
