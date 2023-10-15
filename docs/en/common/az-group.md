---
layout: page
title: common/az-group (English)
description: "Manage resource groups and template deployments."
content_hash: 6328563a37a90393efa2b66add49d8017e470413
last_modified_at: 2023-10-15
related_topics:
  - title: español version
    url: /es/common/az-group.html
    icon: bi bi-globe
---
# az group

Manage resource groups and template deployments.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/group>.

- Create a new resource group:

`az group create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>

- Check if a resource group exists:

`az group exists --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a resource group:

`az group delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Wait until a condition of the resource group is met:

`az group wait --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
