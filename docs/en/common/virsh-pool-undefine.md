---
layout: page
title: common/virsh-pool-undefine (English)
description: "Delete the configuration file in `/etc/libvirt/storage` for a stopped virtual machine storage pool."
content_hash: 18b72a459a4411fbbdee6d0910d3a30bcb3357a3
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-pool-undefine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-undefine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-undefine

Delete the configuration file in `/etc/libvirt/storage` for a stopped virtual machine storage pool.
See also: `virsh`, `virsh-pool-destroy`.
More information: <https://manned.org/virsh>.

- Delete the configuration for the storage pool specified name or UUID (determine using `virsh pool-list`):

`virsh pool-undefine --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
