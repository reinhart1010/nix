---
layout: page
title: common/kubectl-delete (English)
description: "Delete Kubernetes resources."
content_hash: c1f57f52eeb4d073cd1ff2e19f39bfe546853d2d
---
# kubectl delete

Delete Kubernetes resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Delete a specific pod:

`kubectl delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Delete a specific deployment:

`kubect delete deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

- Delete a specific node:

`kubectl delete node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>

- Delete all pods in a specified namespace:

`kubectl delete pods --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Delete all deployments and services in a specified namespace:

`kubectl delete deployments,services --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Delete all nodes:

`kubectl delete nodes --all`

- Delete resources defined in a YAML manifest:

`kubectl delete --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/manifest.yaml</span>
