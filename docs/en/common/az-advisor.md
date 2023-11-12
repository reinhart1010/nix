---
layout: page
title: common/az-advisor (English)
description: "Manage Azure subscription information."
content_hash: 22bc05fcdf48122265e157f28ad977f5ccff1077
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# az advisor

Manage Azure subscription information.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/advisor>.

- List Azure Advisor configuration for the entire subscription:

`az advisor configuration list`

- Show Azure Advisor configuration for the given subscription or resource group:

`az advisor configuration show --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- List Azure Advisor recommendations:

`az advisor recommendation list`

- Enable Azure Advisor recommendations:

`az advisor recommendation enable --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Disable Azure Advisor recommendations:

`az advisor recommendation disable --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
