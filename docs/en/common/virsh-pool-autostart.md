---
layout: page
title: common/virsh-pool-autostart (English)
description: "Enable or disable autostart for a virtual machine storage pool."
content_hash: 269b3d627ec32fe8fa2700994c3e21a4e745c064
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-pool-autostart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-autostart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-autostart

Enable or disable autostart for a virtual machine storage pool.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- Enable autostart for the storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>

- Disable autostart for the storage pool specified by name or UUID:

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --disable`
