---
layout: page
title: linux/efibootmgr (English)
description: "Manipulate the UEFI Boot Manager."
content_hash: 1b8879c9f2594b8f102ea883d2bd889e5f8a11af
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# efibootmgr

Manipulate the UEFI Boot Manager.
More information: <https://manned.org/efibootmgr>.

- List the current settings then bootnums with their name:

`efibootmgr`

- List the filepaths:

`efibootmgr -v`

- Add UEFI Shell v2 as a boot option:

`sudo efibootmgr -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\EFI\tools\Shell.efi</span>` -L "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI Shell</span>`"`

- Change the current boot order:

`sudo efibootmgr -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0002,0008,0001,0005</span>

- Delete a boot option:

`sudo efibootmgr -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0008</span>` --delete-bootnum`
