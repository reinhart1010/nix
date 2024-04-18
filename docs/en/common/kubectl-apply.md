---
layout: page
title: common/kubectl-apply (English)
description: "Manage applications through files defining Kubernetes resources."
content_hash: 63f88a695ef1bb6215f407c7d1be24a9085d997b
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# kubectl apply

Manage applications through files defining Kubernetes resources.
Create and update resources in a cluster.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

- Apply a configuration to a resource by file name or `stdin`:

`kubectl apply -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- Edit the latest last-applied-configuration annotations of resources from the default editor:

`kubectl apply edit-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- Set the latest last-applied-configuration annotations by setting it to match the contents of a file:

`kubectl apply set-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>

- View the latest last-applied-configuration annotations by type/name or file:

`kubectl apply view-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_filename</span>
