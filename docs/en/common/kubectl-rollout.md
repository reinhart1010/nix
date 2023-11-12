---
layout: page
title: common/kubectl-rollout (English)
description: "Manage the rollout of a Kubernetes resource (deployments, daemonsets, and statefulsets)."
content_hash: f1eed6ef67e82a2c1b9bf1df5c9d0fdb921622e3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-rollout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl rollout

Manage the rollout of a Kubernetes resource (deployments, daemonsets, and statefulsets).
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- Start a rolling restart of a resource:

`kubectl rollout restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Watch the rolling update status of a resource:

`kubectl rollout status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Roll back a resource to the previous revision:

`kubectl rollout undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- View the rollout history of a resource:

`kubectl rollout history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>
