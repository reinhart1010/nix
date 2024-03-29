---
layout: page
title: common/az-storage (English)
description: "Manage Azure Cloud Storage resources."
content_hash: 9ea27ffcb5da2eab146d77056e11abaccdb9c500
last_modified_at: 2024-02-09
related_topics:
  - title: español version
    url: /es/common/az-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az storage

Manage Azure Cloud Storage resources.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/storage>.

- Create a storage account specifying a [l]ocation:

`az storage account create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>` --sku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_sku</span>

- List all storage accounts in a resource group:

`az storage account list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- List the access keys for a storage account:

`az storage account keys list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>

- Delete a storage account:

`az storage account delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>

- Update the minimum tls version setting for a storage account:

`az storage account update --min-tls-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLS1_0|TLS1_1|TLS1_2</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>
