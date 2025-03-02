---
layout: page
title: common/kubeadm (English)
description: "Command-line interface for creating and managing Kubernetes clusters."
content_hash: f25b2f4970031fc430f02935598423d07fb80d33
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/kubeadm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kubeadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubeadm

Command-line interface for creating and managing Kubernetes clusters.
More information: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Create a Kubernetes control plane:

`kubeadm init`

- Bootstrap a Kubernetes worker node and join it to a cluster:

`kubeadm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Create a new bootstrap token with a TTL of 12 hours:

`kubeadm token create --ttl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12h0m0s</span>

- Check if the Kubernetes cluster is upgradeable and which versions are available:

`kubeadm upgrade plan`

- Upgrade Kubernetes cluster to a specified version:

`kubeadm upgrade apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- View the kubeadm ConfigMap containing the cluster's configuration:

`kubeadm config view`

- Revert changes made to the host by 'kubeadm init' or 'kubeadm join':

`kubeadm reset`
