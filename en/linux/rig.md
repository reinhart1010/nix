---
layout: page
title: linux/rig (English)
description: "Utility to piece together a random first name, last name, street number and address, along with a geographically consistent (ie, they all match the same area) city, state, ZIP code, and area code."
content_hash: e8586142d4b13a0851bfc33e8e9baf8e7d31a72f
related_topics:
  - title: español version
    url: /es/linux/rig.html
    icon: bi bi-globe
---
# rig

Utility to piece together a random first name, last name, street number and address, along with a geographically consistent (ie, they all match the same area) city, state, ZIP code, and area code.
More information: <https://manpages.ubuntu.com/manpages/focal/man6/rig.6.html>.

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
