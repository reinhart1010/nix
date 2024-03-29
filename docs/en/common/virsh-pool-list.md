---
layout: page
title: common/virsh-pool-list (English)
description: "List information about virtual machine storage pools."
content_hash: 91878c964c06c2b9a7660ca7c905424e544a62de
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-pool-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-list

List information about virtual machine storage pools.
See also: `virsh`, `virsh-pool-autostart`, `virsh-pool-define-as`.
More information: <https://manned.org/virsh>.

- List the name, state, and whether autostart is enabled or disabled for active storage pools:

`virsh pool-list`

- List information for active and inactive or just inactive storage pools:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|inactive</span>

- List extended information about persistence, capacity, allocation, and available space for active storage pools:

`virsh pool-list --details`

- List information for active storage pools with either autostart enabled or disabled:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autostart|no-autostart</span>

- List information for active storage pools that are either persistent or transient:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">persistent|transient</span>

- List the name and UUID of active storage pools:

`virsh pool-list --name --uuid`
