---
layout: page
title: common/kube-capacity (English)
description: "A simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster."
content_hash: 1182654b9b80ee3d5f5a8443134301aba6847e8f
---
# kube-capacity

A simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster.
Combine the best parts of `kubectl top` and `kubectl describe` into a CLI focused on cluster resources.
More information: <https://github.com/robscott/kube-capacity>.

- Output a list of nodes with the total CPU and Memory resource requests and limits:

`kube-capacity`

- Include pods:

`kube-capacity -p`

- Include utilization:

`kube-capacity -u`
