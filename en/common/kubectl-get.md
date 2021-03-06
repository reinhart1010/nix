---
layout: page
title: common/kubectl-get (English)
description: "Get Kubernetes objects and resources."
content_hash: d22cce7916a25d144f3a80704f7e0fb908b1ab31
---
# kubectl get

Get Kubernetes objects and resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Get all namespaces in the current cluster:

`kubectl get namespaces`

- Get nodes in a specified namespace:

`kubectl get nodes -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get pods in a specified namespace:

`kubectl get pods -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get deployments in a specified namespace:

`kubectl get deployments -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get services in a specified namespace:

`kubectl get services -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get all resources in a specified namespace:

`kubectl get all -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Get Kubernetes objects defined in a YAML manifest:

`kubectl get -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest</span>`.yaml`
