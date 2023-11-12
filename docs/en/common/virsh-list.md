---
layout: page
title: common/virsh-list (English)
description: "List the ID, name, and state of virtual machines."
content_hash: 1acf13c592cdc28f11e046e34680d00d0a6d7523
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-list

List the ID, name, and state of virtual machines.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- List information about running virtual machines:

`virsh list`

- List information about virtual machines regardless of state:

`virsh list --all`

- List information about virtual machines with autostart either enabled or disabled:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autostart|no-autostart</span>

- List information about virtual machines either with or without snapshots:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">with-snapshot|without-snapshot</span>
