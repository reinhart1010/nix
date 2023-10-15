---
layout: page
title: common/az-storage-queue (English)
description: "Manage storage queues in Azure."
content_hash: e9aa5003f0572be49f22f6b0d1e70b2bbab221a3
last_modified_at: 2023-10-15
---
# az storage queue

Manage storage queues in Azure.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/storage/queue>.

- Create a queue:

`az storage queue create --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_metadata</span>

- Generate a shared access signature for the queue:

`az storage queue generate-sas --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --permissions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_permissions</span>` --expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expiry_date</span>` --https-only`

- List queues in a storage account:

`az storage queue list --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter_prefix</span>` --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>

- Delete the specified queue and any messages it contains:

`az storage queue delete --account-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queue_name</span>` --fail-not-exist`
