---
layout: page
title: linux/grub-install (中文)
description: "安装 GRUB 到设备。"
content_hash: de84007e5d1c740f54f5fcd77e5e5653756a6549
related_topics:
  - title: English version
    url: /en/linux/grub-install.html
    icon: bi bi-globe
---
# grub-install

安装 GRUB 到设备。
更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- 安装 GRUB 到基于 BIOS 的系统：

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-pc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 安装 GRUB 到基于 UEFI 的系统：

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/efi_directory</span>` --bootloader-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GRUB</span>

- 安装预置指定模块的 GRUB:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/efi_directory</span>` --modules="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part_gpt part_msdos</span>`"`
