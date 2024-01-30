---
layout: page
title: common/fluxctl (English)
description: "Command-line tool for Flux v1."
content_hash: d7b685a561a346a7a82ace48625c4a27780789ef
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# fluxctl

Command-line tool for Flux v1.
More information: <https://fluxcd.io/legacy/flux/references/fluxctl>.

- List workloads currently running in the cluster on specific namespace:

`fluxctl --k8s-fwd-ns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` list-workloads`

- Show deployed and available images:

`fluxctl list-images`

- Synchronize the cluster with the Git repository:

`fluxctl sync`

- Turn on automatic deployment for a workload:

`fluxctl automate`
