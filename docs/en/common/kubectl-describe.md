---
layout: page
title: common/kubectl-describe (English)
description: "Show details of Kubernetes objects and resources."
content_hash: 764dd6e93fe9e0e7415fbb19275b926205525552
last_modified_at: 2023-12-27
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl describe

Show details of Kubernetes objects and resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Show details of pods in a [n]amespace:

`kubectl describe pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show details of nodes in a [n]amespace:

`kubectl describe nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show the details of a specific pod in a [n]amespace:

`kubectl describe pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show the details of a specific node in a [n]amespace:

`kubectl describe nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show details of Kubernetes objects defined in a YAML manifest [f]ile:

`kubectl describe --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest.yaml</span>
