---
layout: page
title: common/kompose (English)
description: "Convert docker-compose applications to Kubernetes."
content_hash: 2aade85fee1a3b7b9b9613dfc1500bef9327b767
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# kompose

Convert docker-compose applications to Kubernetes.
More information: <https://github.com/kubernetes/kompose>.

- Deploy a dockerized application to Kubernetes:

`kompose up -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- Delete instantiated services/deployments from Kubernetes:

`kompose down -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- Convert a docker-compose file into Kubernetes resources file:

`kompose convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>
