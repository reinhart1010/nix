---
layout: page
title: common/virsh-pool-info (English)
description: "List information about a virtual machine storage pool."
content_hash: 1f7f5f44c09d500d43ad1ff7cb5440fe0c25a1ca
---
# virsh pool-info

List information about a virtual machine storage pool.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- List the name, UUID, state, persistence type, autostart status, capacity, space allocated, and space available for the storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-info --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
