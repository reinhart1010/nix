---
layout: page
title: common/kubectl-edit (English)
description: "Edit Kubernetes resources."
content_hash: adc82d0a856c6ff099d534f9bc482c3b768ffab3
last_modified_at: 2023-05-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectl edit

Edit Kubernetes resources.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#edit>.

- Edit a pod:

`kubectl edit pod/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Edit a deployment:

`kubectl edit deployment/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

- Edit a service:

`kubectl edit svc/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Edit a resource using a specific editor:

`KUBE_EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano</span>` kubectl edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Edit a resource in JSON format:

`kubectl edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>` --output json`
