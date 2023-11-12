---
layout: page
title: linux/grub-bios-setup (English)
description: "Set up a device to use GRUB with a BIOS configuration."
content_hash: b76c85042a22fe48d2642e36f2214a4f523d2923
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grub-bios-setup

Set up a device to use GRUB with a BIOS configuration.
You should use `grub-install` instead of `grub-bios-setup` in most cases.
More information: <https://manned.org/grub-bios-setup.8>.

- Set up a device to boot with GRUB:

`grub-bios-setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Install even if problems are detected:

`grub-bios-setup --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Install GRUB in a specific directory:

`grub-bios-setup --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
