---
layout: page
title: common/pvecm (English)
description: "Proxmox VE Cluster Manager."
content_hash: 631f00b6a27a2871075e579588070f21a2af31d8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pvecm

Proxmox VE Cluster Manager.
More information: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Add the current node to an existing cluster:

`pvecm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname_or_ip</span>

- Add a node to the cluster configuration (internal use):

`pvecm addnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>

- Return the version of the cluster join API available on this node:

`pvecm apiver`

- Generate new cluster configuration:

`pvecm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clustername</span>

- Remove a node from the cluster configuration:

`pvecm delnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>

- Display the local view of the cluster nodes:

`pvecm nodes`

- Display the local view of the cluster status:

`pvecm status`
