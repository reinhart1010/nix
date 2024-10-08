---
layout: page
title: linux/pvecm (English)
description: "Proxmox VE Cluster Manager."
content_hash: 6feb3edd9ad3cf1f97dd3952da12bea966015775
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# pvecm

Proxmox VE Cluster Manager.
More information: <https://pve.proxmox.com/pve-docs/pvecm.1.html>.

- Add the current node to an existing cluster:

`pvecm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname_or_ip</span>

- Add a node to the cluster configuration (internal use):

`pvecm addnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>

- Display the version of the cluster join API available on this node:

`pvecm apiver`

- Generate new cluster configuration:

`pvecm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clustername</span>

- Remove a node from the cluster configuration:

`pvecm delnode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>

- Display the local view of the cluster nodes:

`pvecm nodes`

- Display the local view of the cluster status:

`pvecm status`
