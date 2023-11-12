---
layout: page
title: common/kubectl-delete (English)
description: "Delete Kubernetes resources."
content_hash: 33e99e6c011bcdc7dea8fbc736a8ff83ec18e0b7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl delete

Delete Kubernetes resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Delete a specific pod:

`kubectl delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Delete a specific deployment:

`kubectl delete deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

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
