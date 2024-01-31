---
layout: page
title: common/kube-capacity (English)
description: "Provide an overview of resource requests, limits, and utilization in a Kubernetes cluster."
content_hash: 33b292adf84f2f77db43f985e6adf7a9aee7fd32
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# kube-capacity

Provide an overview of resource requests, limits, and utilization in a Kubernetes cluster.
Combine the best parts of `kubectl top` and `kubectl describe` into a CLI focused on cluster resources.
More information: <https://github.com/robscott/kube-capacity>.

- List nodes including the total CPU and Memory resource requests and limits:

`kube-capacity`

- Include pods:

`kube-capacity -p`

- Include utilization:

`kube-capacity -u`
