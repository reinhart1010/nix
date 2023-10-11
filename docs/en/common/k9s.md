---
layout: page
title: common/k9s (English)
description: "View and manage Kubernetes clusters."
content_hash: a68177dd9756589c932affcf0b52c56b555b666d
last_modified_at: 2023-10-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># k9s

View and manage Kubernetes clusters.
More information: <https://k9scli.io/topics/commands/>.

- Manage a cluster using a kubeconfig context:

`k9s --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kubeconfig_context_name</span>

- Manage a cluster in read-only mode (disabling all commands that may cause modifications):

`k9s --readonly --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Manage a cluster using a given kubernetes namespace:

`k9s --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kubernetes_namespace</span>` --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Manage a cluster launching k9s in the pod view and enable debug logging:

`k9s --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod</span>` --logLevel debug --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>
