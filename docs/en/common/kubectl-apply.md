---
layout: page
title: common/kubectl-apply (English)
description: "Manages applications through files defining Kubernetes resources. It creates and updates resources in a cluster."
content_hash: 5bd24846e9a31d312100b5e88e82412563dd78b1
last_modified_at: 2023-10-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectl apply

Manages applications through files defining Kubernetes resources. It creates and updates resources in a cluster.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

- Apply a configuration to a resource by file name or `stdin`:

`kubectl apply -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- Edit the latest last-applied-configuration annotations of resources from the default editor:

`kubectl apply edit-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- Set the latest last-applied-configuration annotations by setting it to match the contents of a file:

`kubectl apply set-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- View the latest last-applied-configuration annotations by type/name or file:

`kubectl apply view-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>
