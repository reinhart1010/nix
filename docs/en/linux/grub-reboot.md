---
layout: page
title: linux/grub-reboot (English)
description: "Set the default boot entry for GRUB, for the next boot only."
content_hash: 145b04208eaddf61512e038b57a61d88c88c07c3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grub-reboot

Set the default boot entry for GRUB, for the next boot only.
More information: <https://manned.org/grub-reboot>.

- Set the default boot entry to an entry number, name or identifier for the next boot:

`sudo grub-reboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_number</span>

- Set the default boot entry to an entry number, name or identifier for an alternative boot directory for the next boot:

`sudo grub-reboot --boot-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/boot_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_number</span>
