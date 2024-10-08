---
layout: page
title: common/linode-cli-volumes (Nederlands)
description: "Beheer Linode Volumes."
content_hash: 23de86d81bab46ee77baed997a9d8bae78a4553c
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-volumes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli volumes

Beheer Linode Volumes.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>.

- Toon alle huidige Volumes:

`linode-cli volumes list`

- Maak een nieuw Volume en koppel het aan een specifieke Linode:

`linode-cli volumes create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_GB</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Koppel een Volume aan een specifieke Linode:

`linode-cli volumes attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` --linode-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Koppel een Volume los van een Linode:

`linode-cli volumes detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>

- Vergroot een Volume (Let op: de grootte kan alleen toenemen):

`linode-cli volumes resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_size_in_GB</span>

- Verwijder een Volume:

`linode-cli volumes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>
