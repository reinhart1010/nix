---
layout: page
title: linux/grub-set-default (English)
description: "Set the default boot entry for GRUB."
content_hash: f174d92e1be9ca0ff12f698ae670c3a203b0a829
last_modified_at: 2023-03-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># grub-set-default

Set the default boot entry for GRUB.
More information: <https://manned.org/grub-set-default>.

- Set the default boot entry to an entry number, name or identifier:

`sudo grub-set-default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_number</span>

- Set the default boot entry to an entry number, name or identifier for an alternative boot directory:

`sudo grub-set-default --boot-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/boot_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_number</span>
