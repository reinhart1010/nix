---
layout: page
title: common/virsh-pool-start (English)
description: "Start a previously configured but inactive virtual machine storage pool."
content_hash: deed846789ee46003f52f72efda6e4db42d1096f
---
# virsh pool-start

Start a previously configured but inactive virtual machine storage pool.
See also: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
More information: <https://manned.org/virsh>.

- Start the storage pool specified by name or UUID (determine using `virsh pool-list`) and create the underlying storage system if it doesn't exist:

`virsh pool-start --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --build`
