---
layout: page
title: windows/azcopy (English)
description: "A file transfer tool for uploading to Azure Cloud Storage Accounts."
content_hash: aa98ee51545d24934a5c9b5ca7871fb5160824d3
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/windows/azcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# azcopy

A file transfer tool for uploading to Azure Cloud Storage Accounts.
More information: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Log in to an Azure Tenant:

`azopy login`

- Upload a local file:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blob_name</span>`'`

- Upload files with `.txt` and `.jpg` extensions:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`' --include-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt;*.jpg</span>`'`

- Copy a container directly between two Azure storage accounts:

`azcopy copy 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_storage_account_name</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_storage_account_name</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`'`

- Synchronize a local directory and delete files in the destination if they no longer exist in the source:

`azcopy sync '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_account_name</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`' --recursive --delete-destination=true`

- Display detailed usage information:

`azcopy --help`
