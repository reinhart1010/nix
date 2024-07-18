---
layout: page
title: linux/sbctl (English)
description: "A user-friendly secure boot key manager."
content_hash: b600189e180a12998b504bab0bffab63c8bc9ae7
last_modified_at: 2024-07-18
tldri18n_status: 2
---
# sbctl

A user-friendly secure boot key manager.
Note: not enrolling Microsoft's certificates can brick your system. See <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>.
More information: <https://github.com/Foxboron/sbctl#usage>.

- Show the current secure boot status:

`sbctl status`

- Create custom secure boot keys (everything is stored in `/usr/share/secureboot`):

`sbctl create-keys`

- Enroll the custom secure boot keys and Microsoft's UEFI vendor certificates:

`sbctl enroll-keys --microsoft`

- Sign an EFI binary with the created key and save the file to the database:

`sbctl sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--save</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/efi_binary</span>

- Re-sign all the saved files:

`sbctl sign-all`

- Verify that all EFI executables on the EFI system partition have been signed:

`sbctl verify`
