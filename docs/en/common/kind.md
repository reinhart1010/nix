---
layout: page
title: common/kind (English)
description: "Run local Kubernetes clusters using Docker container \"nodes\"."
content_hash: 8155b9cf995d74da4b23a89d8d46b4c5c9e5740a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# kind

Run local Kubernetes clusters using Docker container "nodes".
Designed for testing Kubernetes itself, but may be used for local development or continuous integration.
More information: <https://github.com/kubernetes-sigs/kind>.

- Create a local Kubernetes cluster:

`kind create cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Delete one or more clusters:

`kind delete clusters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Get details about clusters, nodes, or the kubeconfig:

`kind get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clusters|nodes|kubeconfig</span>

- Export the kubeconfig or the logs:

`kind export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kubeconfig|logs</span>
