---
layout: page
title: linux/aa-complain (English)
description: "Set an AppArmor policy to complain mode."
content_hash: 8649f1f05746033b4ee177dae311e8eed06c3cce
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/linux/aa-complain.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-complain

Set an AppArmor policy to complain mode.
See also: `aa-disable`, `aa-enforce`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Set policy to complain mode:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile1 path/to/profile2 ...</span>

- Set policies to complain mode:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profiles</span>
