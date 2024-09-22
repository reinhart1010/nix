---
layout: page
title: linux/bcachefs-device (English)
description: "Manage devices within a running `bcachefs` filesystem."
content_hash: d1c55fa6193c8fea1be1d6bf9042bbc18266f20d
last_modified_at: 2024-09-22
tldri18n_status: 2
---
# bcachefs device

Manage devices within a running `bcachefs` filesystem.
More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- Format and add a new device to an existing filesystem.:

`sudo bcachefs device add --label=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Migrate data off a device to prepare for removal:

`bcachefs device evacuate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Permanently remove a device from a filesystem:

`bcachefs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>
