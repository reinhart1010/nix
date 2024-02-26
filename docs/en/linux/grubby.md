---
layout: page
title: linux/grubby (English)
description: "Tool for configuring `grub` and `zipl` bootloaders."
content_hash: b449e53e21930277ac258ecf3eab5012c62ebbc7
last_modified_at: 2024-02-26
tldri18n_status: 2
---
# grubby

Tool for configuring `grub` and `zipl` bootloaders.
More information: <https://manned.org/man/grubby.8>.

- Add kernel boot arguments to all kernel menu entries:

`sudo grubby --update-kernel=ALL --args '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet console=ttyS0</span>`'`

- Remove existing arguments from the entry for the default kernel:

`sudo grubby --update-kernel=DEFAULT --remove-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet</span>

- List all kernel menu entries:

`sudo grubby --info=ALL`
