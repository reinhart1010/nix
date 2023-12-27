---
layout: page
title: common/kubectl-get (English)
description: "Get Kubernetes objects and resources."
content_hash: e308bd789c695a8607623ec7a1e5984ec721f820
last_modified_at: 2023-12-27
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl get

Get Kubernetes objects and resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Get all namespaces in the current cluster:

`kubectl get namespaces`

- Get nodes in a specified [n]amespace:

`kubectl get nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get pods in a specified [n]amespace:

`kubectl get pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get deployments in a specified [n]amespace:

`kubectl get deployments --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get services in a specified [n]amespace:

`kubectl get services --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get all resources in a specified [n]amespace:

`kubectl get all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get Kubernetes objects defined in a YAML manifest [f]ile:

`kubectl get --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest.yaml</span>
