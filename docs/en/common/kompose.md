---
layout: page
title: common/kompose (English)
description: "A tool to convert docker-compose applications to Kubernetes."
content_hash: fad9d6c2d854df264091024864cca741662e0d68
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kompose

A tool to convert docker-compose applications to Kubernetes.
More information: <https://github.com/kubernetes/kompose>.

- Deploy a dockerized application to Kubernetes:

`kompose up -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- Delete instantiated services/deployments from Kubernetes:

`kompose down -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- Convert a docker-compose file into Kubernetes resources file:

`kompose convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>
