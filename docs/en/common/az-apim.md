---
layout: page
title: common/az-apim (English)
description: "Manage Azure API Management services."
content_hash: 1b438b323ced3b62a5df5d237c59f5202ae9f89f
last_modified_at: 2023-10-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az apim

Manage Azure API Management services.
Part of `az`.
More information: <https://docs.microsoft.com/cli/azure/apim>.

- List API Management services within a resource group:

`az apim list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Create an API Management service instance:

`az apim create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>` --publisher-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` --publisher-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete an API Management service:

`az apim delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Show details of an API Management service instance:

`az apim show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>

- Update an API Management service instance:

`az apim update --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
