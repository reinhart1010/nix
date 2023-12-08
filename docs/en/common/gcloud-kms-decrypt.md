---
layout: page
title: common/gcloud-kms-decrypt (English)
description: "Decrypt a ciphertext file using a Cloud KMS key."
content_hash: f1dccdfc38b364873cb52e11784f72d272b638eb
last_modified_at: 2023-12-08
tldri18n_status: 2
---
# gcloud kms decrypt

Decrypt a ciphertext file using a Cloud KMS key.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- Decrypt a file using a specified key, key ring, and location:

`gcloud kms decrypt --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` --keyring=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyring_name</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` --ciphertext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ciphertext</span>` --plaintext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/plaintext</span>

- Decrypt a file with additional authenticated data (AAD) and write the decrypted plaintext to `stdout`:

`gcloud kms decrypt --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>` --keyring=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyring_name</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` --additional-authenticated-data-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.aad</span>` --ciphertext-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ciphertext</span>` --plaintext-file=-`
