---
layout: page
title: common/linode-cli-lke (Nederlands)
description: "Beheer Linode Kubernetes Engine (LKE) clusters."
content_hash: 3160dd053814091a19e863eb93654284e7790965
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-lke.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli lke

Beheer Linode Kubernetes Engine (LKE) clusters.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-lke>.

- Toon alle LKE clusters:

`linode-cli lke clusters list`

- Maak een nieuw LKE cluster:

`linode-cli lke clusters create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_type</span>` --nodes-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Toon details van een specifiek LKE cluster:

`linode-cli lke clusters view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>

- Update een bestaand LKE cluster:

`linode-cli lke clusters update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` --node-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_node_type</span>

- Verwijder een LKE cluster:

`linode-cli lke clusters delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>
