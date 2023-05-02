---
layout: page
title: linux/bootctl (English)
description: "Control EFI firmware boot settings and manage boot loader."
content_hash: 9f79d754e63364abf2eaf2762ce37da4a0adbd8f
last_modified_at: 2023-05-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bootctl

Control EFI firmware boot settings and manage boot loader.
More information: <https://manned.org/bootctl>.

- Show information about the system firmware and the bootloaders:

`bootctl status`

- Show all available bootloader entries:

`bootctl list`

- Set a flag to boot into the system firmware on the next boot (similar to `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Specify the path to the EFI system partition (defaults to `/efi/`, `/boot/` or `/boot/efi`):

`bootctl --esp-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/efi_system_partition/</span>

- Install `systemd-boot` into the EFI system partition:

`sudo bootctl install`

- Remove all installed versions of `systemd-boot` from the EFI system partition:

`sudo bootctl remove`
