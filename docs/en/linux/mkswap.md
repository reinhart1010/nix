---
layout: page
title: linux/mkswap (English)
description: "Sets up a Linux swap area on a device or in a file."
content_hash: e0cf0ce40b7da7b58952d624c822397051bdc72a
---
# mkswap

Sets up a Linux swap area on a device or in a file.
More information: <https://manned.org/mkswap>.

- Setup a given partition as swap area:

`sudo mkswap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb7</span>

- Use a given file as swap area:

`sudo mkswap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check a partition for bad blocks before creating the swap area:

`sudo mkswap -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb7</span>

- Specify a label for the file (to allow `swapon` to use the label):

`sudo mkswap -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swap1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
