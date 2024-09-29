---
layout: page
title: common/linode-cli-object-storage (Nederlands)
description: "Beheer Linode Object Storage."
content_hash: 5e63b0b5c08c44e437bac3593acb90d4485b2ec4
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-object-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli object-storage

Beheer Linode Object Storage.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>.

- Toon alle Object Storage buckets:

`linode-cli object-storage buckets list`

- Maak een nieuwe Object Storage bucket:

`linode-cli object-storage buckets create --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_label</span>

- Verwijder een Object Storage bucket:

`linode-cli object-storage buckets delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_label</span>

- Toon alle Object Storage cluster regio's:

`linode-cli object-storage clusters list`

- Toon alle access keys voor Object Storage:

`linode-cli object-storage keys list`

- Maak een nieuw access key voor Object Storage:

`linode-cli object-storage keys create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>

- Trek een access key terug voor Object Storage:

`linode-cli object-storage keys revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_key_id</span>
