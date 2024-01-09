---
layout: page
title: common/gcloud-container (English)
description: "Manage containerized applications on Kubernetes and clusters."
content_hash: e5240b03b7582d3e86d903f29b3e5400a9bd2079
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# gcloud container

Manage containerized applications on Kubernetes and clusters.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/container>.

- Register `gcloud` as a Docker credential helper:

`gcloud auth configure-docker`

- Create a cluster to run GKE containers:

`gcloud container clusters create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- List clusters for running GKE containers:

`gcloud container clusters list`

- Update kubeconfig to get `kubectl` to use a GKE cluster:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- List tag and digest metadata for a container image:

`gcloud container images list-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
