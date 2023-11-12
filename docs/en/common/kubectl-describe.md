---
layout: page
title: common/kubectl-describe (English)
description: "Show details of Kubernetes objects and resources."
content_hash: f59ae08dd86da9647154bc05dbb62d2e1601468c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl describe

Show details of Kubernetes objects and resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Show details of pods in a namespace:

`kubectl describe pods -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show details of nodes in a namespace:

`kubectl describe nodes -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show the details of a specific pod in a namespace:

`kubectl describe pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show the details of a specific node in a namespace:

`kubectl describe nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Show details of Kubernetes objects defined in a YAML manifest:

`kubectl describe -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest.yaml</span>
