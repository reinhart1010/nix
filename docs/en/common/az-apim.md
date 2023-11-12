---
layout: page
title: common/az-apim (English)
description: "Manage Azure API Management services."
content_hash: 8981ae06e3fbe8edf8dfede7a9b97bb13fce3290
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/az-apim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az apim

Manage Azure API Management services.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/apim>.

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
