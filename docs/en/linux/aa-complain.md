---
layout: page
title: linux/aa-complain (English)
description: "Set an AppArmor policy to complain mode."
content_hash: d3b0e7b67c7b37a3101d6d951154caf1eb0c5b0f
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aa-complain

Set an AppArmor policy to complain mode.
See also: `aa-disable`, `aa-enforce`, `aa-status`.
More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Set policy to complain mode:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile</span>

- Set policies to complain mode:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profiles</span>
