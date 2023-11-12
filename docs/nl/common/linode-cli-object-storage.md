---
layout: page
title: common/linode-cli-object-storage (Nederlands)
description: "Beheer Linode Object Storage."
content_hash: 6ab6501dac0b97a8f7158a791e2211694825ed2a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/linode-cli-object-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli object-storage

Beheer Linode Object Storage.
Bekijk ook: `linode-cli`.
Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/object-storage/>.

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
