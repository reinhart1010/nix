---
layout: page
title: linux/rig (English)
description: "Utility to piece together a random first name, last name, street number and address, along with a geographically consistent (ie, they all match the same area) city, state, ZIP code, and area code."
content_hash: 0eb9949fca77cf0119d9d54e81610bde395859a3
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/rig.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/rig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rig

Utility to piece together a random first name, last name, street number and address, along with a geographically consistent (ie, they all match the same area) city, state, ZIP code, and area code.
More information: <https://manned.org/rig>.

- Display a random name (male or female) and address:

`rig`

- Display a [m]ale (or [f]emale) random name and address:

`rig -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m|f</span>

- Use data files from a specific directory (default is `/usr/share/rig`):

`rig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display a specific number of identities:

`rig -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Display a specific number of female identities:

`rig -f -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>
