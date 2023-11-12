---
layout: page
title: common/kube-capacity (English)
description: "Provide an overview of resource requests, limits, and utilization in a Kubernetes cluster."
content_hash: b08b338a52894cd6929263b5d998edff69186466
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kube-capacity

Provide an overview of resource requests, limits, and utilization in a Kubernetes cluster.
Combine the best parts of `kubectl top` and `kubectl describe` into a CLI focused on cluster resources.
More information: <https://github.com/robscott/kube-capacity>.

- Output a list of nodes with the total CPU and Memory resource requests and limits:

`kube-capacity`

- Include pods:

`kube-capacity -p`

- Include utilization:

`kube-capacity -u`
