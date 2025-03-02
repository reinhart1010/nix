---
layout: page
title: linux/paxs (English)
description: "Manage packages across Yay, Flatpak, and Snap."
content_hash: a3226b84e15184d1c7c03736763003b8028b55c6
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/paxs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paxs

Manage packages across Yay, Flatpak, and Snap.
Supports searching, installing, removing, and upgrading packages.
More information: <https://github.com/zamhedonia/paxs>.

- Search for a package:

`paxs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Upgrade all packages:

`paxs -u`

- Install a package (prompting for the source):

`paxs -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package (prompting for the source):

`paxs -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Check for updates across all package managers:

`paxs -c`

- Display help:

`paxs -h`
