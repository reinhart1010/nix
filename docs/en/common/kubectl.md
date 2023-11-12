---
layout: page
title: common/kubectl (English)
description: "Command-line interface for running commands against Kubernetes clusters."
content_hash: 0645607b6cbc94d6674ea002db6a32cf3aed4ee0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/kubectl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kubectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl

Command-line interface for running commands against Kubernetes clusters.
Some subcommands such as `kubectl run` have their own usage documentation.
More information: <https://kubernetes.io/docs/reference/kubectl/>.

- List information about a resource with more details:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` -o wide`

- Update specified pod with the label 'unhealthy' and the value 'true':

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` unhealthy=true`

- List all resources with different types:

`kubectl get all`

- Display resource (CPU/Memory/Storage) usage of nodes or pods:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|node</span>

- Print the address of the master and cluster services:

`kubectl cluster-info`

- Display an explanation of a specific field:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- Print the logs for a container in a pod or specified resource:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Run command in an existing pod:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
