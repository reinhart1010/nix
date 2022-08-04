---
layout: page
title: common/k8s-unused-secret-detector (English)
description: "Command-line interface tool for detecting unused Kubernetes secrets."
content_hash: 07a1ca935db8fb6e9efe95104ed7f252f293112a
---
# k8s-unused-secret-detector

Command-line interface tool for detecting unused Kubernetes secrets.
More information: <https://github.com/dtan4/k8s-unused-secret-detector>.

- Detect unused secrets:

`k8s-unused-secret-detector`

- Detect unused secrets in a specific namespace:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Delete unused secrets in a specific namespace:

`k8s-unused-secret-detector -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` | kubectl delete secret -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>
