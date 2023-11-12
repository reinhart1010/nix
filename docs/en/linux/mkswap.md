---
layout: page
title: linux/mkswap (English)
description: "Set up a Linux swap area on a device or in a file."
content_hash: 4e9e3cc6ada1fc1af01d127aa60daa559dc78de1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mkswap

Set up a Linux swap area on a device or in a file.
Note: `path/to/file` can either point to a regular file or a swap partition.
More information: <https://manned.org/mkswap>.

- Set up a given swap area:

`sudo mkswap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check a partition for bad blocks before creating the swap area:

`sudo mkswap -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a label for the partition (to allow `swapon` to use the label):

`sudo mkswap -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
