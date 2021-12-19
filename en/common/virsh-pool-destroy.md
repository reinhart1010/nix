---
layout: page
title: common/virsh-pool-destroy (English)
description: "Stop an active virtual machine storage pool."
content_hash: 408930288dd733fd0e5d37cbea8ac67376752172
---
# virsh pool-destroy

Stop an active virtual machine storage pool.
See also: `virsh`, `virsh-pool-delete`.
More information: <https://manned.org/virsh>.

- Stop a storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-destroy --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
