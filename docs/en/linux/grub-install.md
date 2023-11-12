---
layout: page
title: linux/grub-install (English)
description: "Install GRUB to a device."
content_hash: 4999745179c05047cac40b414bc6c10af664ea80
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/grub-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-install

Install GRUB to a device.
More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- Install GRUB on a BIOS system:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-pc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Install GRUB on an UEFI system:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/efi_directory</span>` --bootloader-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GRUB</span>

- Install GRUB pre-loading specific modules:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/efi_directory</span>` --modules="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part_gpt part_msdos</span>`"`
