---
layout: page
title: common/az-appconfig (English)
description: "Manage App configurations on Azure."
content_hash: f1a2953b8b87b49f78e752891cca010cd7ddb41e
---
# az appconfig

Manage App configurations on Azure.
Part of `az`, the command-line client for Microsoft Azure.
More information: <https://docs.microsoft.com/cli/azure/appconfig>.

- Create an App Configuration:

`az appconfig create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>

- Delete a specific App Configuration:

`az appconfig delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appconfig_name</span>

- List all App Configurations under the current subscription:

`az appconfig list`

- List all App Configurations under a specific resource group:

`az appconfig list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg_name</span>

- Show properties of an App Configuration:

`az appconfig show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appconfig_name</span>

- Update a specific App Configuration:

`az appconfig update --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appconfig_name</span>
