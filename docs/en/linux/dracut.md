---
layout: page
title: linux/dracut (English)
description: "Generate initramfs images to boot the Linux kernel."
content_hash: b72f6983041a62887086474ab535d9e18cc6b29d
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# dracut

Generate initramfs images to boot the Linux kernel.
Dracut uses options from configuration files in `/etc/dracut.conf`, `/etc/dracut.conf.d/*.conf` and `/usr/lib/dracut/dracut.conf.d/*.conf` by default.
More information: <https://github.com/dracutdevs/dracut/wiki>.

- Generate an initramfs image for the current kernel without overriding any options:

`dracut`

- Generate an initramfs image for the current kernel and overwrite the existing one:

`dracut --force`

- Generate an initramfs image for a specific kernel:

`dracut --kver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_version</span>

- List available modules:

`dracut --list-modules`
