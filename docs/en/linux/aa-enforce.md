---
layout: page
title: linux/aa-enforce (English)
description: "Set an AppArmor profile to enforce mode."
content_hash: a160aac7bf3e0ffe420f1eb980d8db80da5f7e98
last_modified_at: 2024-10-23
related_topics:
  - title: Nederlands version
    url: /nl/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-enforce

Set an AppArmor profile to enforce mode.
See also: `aa-complain`, `aa-disable`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Enable profile:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>

- Enable profiles:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile1 path/to/profile2 ...</span>
