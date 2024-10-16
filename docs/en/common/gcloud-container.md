---
layout: page
title: common/gcloud-container (English)
description: "Manage containerized applications on Kubernetes and clusters."
content_hash: 607ddcf94d2b222e43db94a2ca8eb5c77f959782
last_modified_at: 2024-10-16
related_topics:
  - title: 한국어 version
    url: /ko/common/gcloud-container.html
    icon: bi bi-globe
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

- Describe an existing cluster for running containers:

`gcloud container clusters describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>
