---
layout: page
title: common/virsh-connect (English)
description: "Connect to a virtual machine hypervisor."
content_hash: 7f993852268657b5dd678e4671e7e0d0a4facc00
last_modified_at: 2024-03-14
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-connect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-connect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-connect

Connect to a virtual machine hypervisor.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- Connect to the default hypervisor:

`virsh connect`

- Connect as root to the local QEMU/KVM hypervisor:

`virsh connect qemu:///system`

- Launch a new instance of the hypervisor and connect to it as the local user:

`virsh connect qemu:///session`

- Connect as root to a remote hypervisor using SSH:

`virsh connect qemu+ssh://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name@host_name</span>`/system`
