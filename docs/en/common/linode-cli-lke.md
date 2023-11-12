---
layout: page
title: common/linode-cli-lke (English)
description: "Manage Linode Kubernetes Engine (LKE) clusters."
content_hash: 0d65fdc6dc73a47fc372f3c04b56063097bef49e
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/common/linode-cli-lke.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli lke

Manage Linode Kubernetes Engine (LKE) clusters.
See also: `linode-cli`.
More information: <https://www.linode.com/docs/products/tools/cli/guides/linode-kubernetes-engine/>.

- List all LKE clusters:

`linode-cli lke clusters list`

- Create a new LKE cluster:

`linode-cli lke clusters create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_type</span>` --nodes-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- View details of a specific LKE cluster:

`linode-cli lke clusters view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>

- Update an existing LKE cluster:

`linode-cli lke clusters update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_node_type</span>

- Delete an LKE cluster:

`linode-cli lke clusters delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>
