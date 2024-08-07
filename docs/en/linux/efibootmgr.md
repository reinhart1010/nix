---
layout: page
title: linux/efibootmgr (English)
description: "Manipulate the UEFI Boot Manager."
content_hash: 262ac3aa9fda0b64a9c32a15b5ee7d81f4603625
last_modified_at: 2024-07-10
tldri18n_status: 2
---
# efibootmgr

Manipulate the UEFI Boot Manager.
More information: <https://manned.org/efibootmgr>.

- List all boot options with their numbers:

`efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unicode</span>

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -l "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\path\to\shell.efi</span>`" -L "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI Shell</span>`"`

- Add Linux as a boot option:

`sudo efibootmgr --create --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` --part `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --loader "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\vmlinuz</span>`" --unicode "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_cmdline</span>`" --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Linux</span>`"`

- Change the current boot order:

`sudo efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--bootorder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0002,0008,0001,0005</span>

- Delete a boot option:

`sudo efibootmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--bootnum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0008</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-B|--delete-bootnum</span>
