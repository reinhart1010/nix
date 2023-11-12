---
layout: page
title: linux/pvcreate (English)
description: "Initialize a disk or partition for use as a physical volume."
content_hash: 7465ed586b1a85896afb73e2de39cdfad3a7ef56
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pvcreate

Initialize a disk or partition for use as a physical volume.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/pvcreate.8.html>.

- Initialize the `/dev/sda1` volume for use by LVM:

`pvcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Force the creation without any confirmation prompts:

`pvcreate --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
