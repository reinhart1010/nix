---
layout: page
title: common/az-group (English)
description: "Manage resource groups and template deployments."
content_hash: 03668c75d7592e06e9d2c3085460ba47a2590755
---
# az group

Manage resource groups and template deployments.
Part of `azure-cli`.
More information: <https://docs.microsoft.com/cli/azure/group>.

- Create a new resource group:

`az group create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>

- Check if a resource group exists:

`az group exists --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a resource group:

`az group delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Wait until a condition of the resource group is met:

`az group wait --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
