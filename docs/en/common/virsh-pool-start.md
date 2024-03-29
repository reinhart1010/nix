---
layout: page
title: common/virsh-pool-start (English)
description: "Start a previously configured but inactive virtual machine storage pool."
content_hash: deed846789ee46003f52f72efda6e4db42d1096f
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-pool-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-pool-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-start

Start a previously configured but inactive virtual machine storage pool.
See also: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
More information: <https://manned.org/virsh>.

- Start the storage pool specified by name or UUID (determine using `virsh pool-list`) and create the underlying storage system if it doesn't exist:

`virsh pool-start --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --build`
