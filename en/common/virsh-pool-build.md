---
layout: page
title: common/virsh-pool-build (English)
description: "Build the underlying storage system for a virtual machine storage pool as defined in it's configuration file in `/etc/libvirt/storage`."
content_hash: 59c9b3681cb17d299a9c3f3e3bef452160245e83
---
# virsh pool-build

Build the underlying storage system for a virtual machine storage pool as defined in it's configuration file in `/etc/libvirt/storage`.
See also: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
More information: <https://manned.org/virsh>.

- Build the storage pool specified by name or UUID (determine using `virsh pool-list`):

`virsh pool-build --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>
