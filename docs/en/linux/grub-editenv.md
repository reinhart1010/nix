---
layout: page
title: linux/grub-editenv (English)
description: "Edit GRUB environment variables."
content_hash: 8676fb136a1719c283119eb848fc09f3872b1de9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grub-editenv

Edit GRUB environment variables.
More information: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- Set a default boot entry (Assuming the boot entry already exists):

`grub-editenv /boot/grub/grubenv set default=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ubuntu</span>

- Display the current value of the `timeout` variable:

`grub-editenv /boot/grub/grubenv list timeout`

- Reset the `saved_entry` variable to the default:

`grub-editenv /boot/grub/grubenv unset saved_entry`

- Append "quiet splash" to the kernel command line:

`grub-editenv /boot/grub/grubenv list kernel_cmdline`
