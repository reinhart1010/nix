---
layout: page
title: linux/pvcreate (English)
description: "Initialize a disk or partition for use as a physical volume."
content_hash: 6698e2dff5757fafc8e3e28c02345324df69538f
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# pvcreate

Initialize a disk or partition for use as a physical volume.
See also: `lvm`.
More information: <https://manned.org/pvcreate>.

- Initialize the `/dev/sda1` volume for use by LVM:

`pvcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Force the creation without any confirmation prompts:

`pvcreate --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
