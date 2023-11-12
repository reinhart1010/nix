---
layout: page
title: common/az-aks (English)
description: "Manage Azure Kubernetes Service (AKS) clusters."
content_hash: c2cc120edca7ec233a951d74e5cb700dab4ceac0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# az aks

Manage Azure Kubernetes Service (AKS) clusters.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/aks>.

- List AKS clusters:

`az aks list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Create a new AKS cluster:

`az aks create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --node-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --node-vm-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Delete an AKS cluster:

`az aks delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Get the access credentials for an AKS cluster:

`az aks get-credentials --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Get the upgrade versions available for an AKS cluster:

`az aks get-upgrades --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
