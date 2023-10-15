---
layout: page
title: common/az-storage-container (English)
description: "Manage blob storage containers in Azure."
content_hash: 8d8c480e40f7d697fbb05bdaa88da3a0566d7a84
last_modified_at: 2023-10-15
---
# az storage container

Manage blob storage containers in Azure.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/storage/container>.

- Create a container in a storage account:

`az storage container create --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --public-access `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_level</span>` --fail-on-exist`

- Generate a shared access signature for the container:

`az storage container generate-sas --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --permissions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sas_permissions</span>` --expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expiry_date</span>` --https-only`

- List containers in a storage account:

`az storage container list --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter_prefix</span>

- Mark the specified container for deletion:

`az storage container delete --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --fail-not-exist`
