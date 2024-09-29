---
layout: page
title: common/linode-cli-linodes (Nederlands)
description: "Beheer Linode instanties."
content_hash: a848bf1a22805f7a152293b1928358bdb7d35bd3
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-linodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli linodes

Beheer Linode instanties.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- Toon alle Linodes:

`linode-cli linodes list`

- Maak een nieuwe Linode:

`linode-cli linodes create --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_type</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_id</span>

- Bekijk details van een specifieke Linode:

`linode-cli linodes view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Werk de instellingen bij voor een Linode:

`linode-cli linodes update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[new_label</span>

- Verwijder een Linode:

`linode-cli linodes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Voer een stroombeheer-operatie uit op een Linode:

`linode-cli linodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">boot|reboot|shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Toon alle beschikbare backups van een Linode:

`linode-cli linodes backups-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Zet een backup terug naar een Linode:

`linode-cli linodes backups-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>` --backup-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_id</span>
