---
layout: page
title: common/az-webapp (English)
description: "Manage Web Applications hosted in Azure Cloud Services."
content_hash: c68ef6afef1fef39643d28ad4e2c42876a9f0115
last_modified_at: 2023-10-15
related_topics:
  - title: español version
    url: /es/common/az-webapp.html
    icon: bi bi-globe
---
# az webapp

Manage Web Applications hosted in Azure Cloud Services.
Part of `azure-cli` (also known as `az`).
Mode information: <https://learn.microsoft.com/cli/azure/webapp>.

- List available runtimes for a web application:

`az webapp list-runtimes --os-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|linux</span>

- Create a web application:

`az webapp up --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime</span>

- List all web applications:

`az webapp list`

- Delete a specific web application:

`az webapp delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_group</span>
