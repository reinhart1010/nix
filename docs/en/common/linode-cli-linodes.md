---
layout: page
title: common/linode-cli-linodes (English)
description: "Manage Linode instances."
content_hash: 8d52b5cdcd64d1c3d6dd4cdd079d7f4d3f61456e
last_modified_at: 2024-09-29
related_topics:
  - title: Nederlands version
    url: /nl/common/linode-cli-linodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli linodes

Manage Linode instances.
See also: `linode-cli`.
More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- List all Linodes:

`linode-cli linodes list`

- Create a new Linode:

`linode-cli linodes create --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_type</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_id</span>

- View details of a specific Linode:

`linode-cli linodes view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Update settings for a Linode:

`linode-cli linodes update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[new_label</span>

- Delete a Linode:

`linode-cli linodes delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Perform a power management operation on a Linode:

`linode-cli linodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">boot|reboot|shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- List available backups for a Linode:

`linode-cli linodes backups-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>

- Restore a backup to a Linode:

`linode-cli linodes backups-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linode_id</span>` --backup-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_id</span>
