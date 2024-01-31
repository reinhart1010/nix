---
layout: page
title: linux/aa-enforce (English)
description: "Set an AppArmor profile to enforce mode."
content_hash: e92453f1f8d7c1901e8193a50f2c18e70f2f97f8
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# aa-enforce

Set an AppArmor profile to enforce mode.
See also: `aa-complain`, `aa-disable`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Enable profile:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile1 path/to/profile2 ...</span>

- Enable profiles:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>
