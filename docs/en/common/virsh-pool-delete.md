---
layout: page
title: common/virsh-pool-delete (English)
description: "Delete the underlying storage system of an inactive virtual machine storage pool."
content_hash: a99707f672c020f291b63fd99e3d074d048bbce0
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-pool-delete.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-delete

Delete the underlying storage system of an inactive virtual machine storage pool.
See also: `virsh`, `virsh-pool-destroy`, `virsh-pool-undefine`.
More information: <https://manned.org/virsh>.

- Delete the underlying storage system for the storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-delete --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
