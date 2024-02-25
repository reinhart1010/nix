---
layout: page
title: common/k8s-unused-secret-detector (English)
description: "Detect unused Kubernetes secrets."
content_hash: 37730e39b1abd0f57adb29a9825d5a0622c3d27b
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# k8s-unused-secret-detector

Detect unused Kubernetes secrets.
More information: <https://github.com/dtan4/k8s-unused-secret-detector>.

- Detect unused secrets:

`k8s-unused-secret-detector`

- Detect unused secrets in a specific namespace:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Delete unused secrets in a specific namespace:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` | kubectl delete secret -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>
