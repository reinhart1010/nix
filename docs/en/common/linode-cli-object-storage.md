---
layout: page
title: common/linode-cli-object-storage (English)
description: "Manage Linode Object Storage."
content_hash: a45d4579266cbc490efdaf2fb027b8d418dd0dab
last_modified_at: 2024-09-29
related_topics:
  - title: Nederlands version
    url: /nl/common/linode-cli-object-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli object-storage

Manage Linode Object Storage.
See also: `linode-cli`.
More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>.

- List all Object Storage buckets:

`linode-cli object-storage buckets list`

- Create a new Object Storage bucket:

`linode-cli object-storage buckets create --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_label</span>

- Delete an Object Storage bucket:

`linode-cli object-storage buckets delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_label</span>

- List Object Storage cluster regions:

`linode-cli object-storage clusters list`

- List access keys for Object Storage:

`linode-cli object-storage keys list`

- Create a new access key for Object Storage:

`linode-cli object-storage keys create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>

- Revoke an access key for Object Storage:

`linode-cli object-storage keys revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_key_id</span>
