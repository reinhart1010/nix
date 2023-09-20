---
layout: page
title: linux/dracut (English)
description: "Generate initramfs images to boot the Linux kernel."
content_hash: d51225e05bd8e346a7090aaca813dbdc01654e6c
last_modified_at: 2023-09-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dracut

Generate initramfs images to boot the Linux kernel.
Dracut uses options from configuration files in `/etc/dracut.conf`, `/etc/dracut.conf.d/*.conf` and `/usr/lib/dracut/dracut.conf.d/*.conf` by default.
More information: <https://github.com/dracutdevs/dracut/wiki>.

- Generate an initramfs image for the current kernel without overriding any options:

`dracut`

- Generate an initramfs image for the current kernel and overwrite the existing one:

`dracut --force`

- Generate an initramfs image for a specific kernel:

`dracut --kver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_version</span>

- Show a list of available modules:

`dracut --list-modules`
