---
layout: page
title: common/rbac-lookup (English)
description: "Find roles and cluster roles attached to any user, service account or group name in your Kubernetes cluster."
content_hash: f07ec67ddd4406c55ce16874f220e9605fff4d64
---
# rbac-lookup

Find roles and cluster roles attached to any user, service account or group name in your Kubernetes cluster.
More information: <https://github.com/reactiveops/rbac-lookup>.

- View all RBAC bindings:

`rbac-lookup`

- View RBAC bindings that match a given expression:

`rbac-lookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- View all RBAC bindings along with the source role binding:

`rbac-lookup -o wide`

- View all RBAC bindings filtered by subject:

`rbac-lookup -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|group|serviceaccount</span>

- View all RBAC bindings along with IAM roles (if you are using GKE):

`rbac-lookup --gke`
