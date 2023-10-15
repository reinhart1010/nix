---
layout: page
title: common/az-storage-table (English)
description: "Manage NoSQL key-value storage in Azure."
content_hash: e7e64ec9328b60e4eb7835e426641d3221af1444
last_modified_at: 2023-10-15
---
# az storage table

Manage NoSQL key-value storage in Azure.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/storage/table>.

- Create a new table in the storage account:

`az storage table create --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --fail-on-exist`

- Generate a shared access signature for the table:

`az storage table generate-sas --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --permissions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sas_permissions</span>` --expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expiry_date</span>` --https-only`

- List tables in a storage account:

`az storage table list --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>

- Delete the specified table and any data it contains:

`az storage table delete --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>` --fail-not-exist`
