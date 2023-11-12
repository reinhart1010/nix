---
layout: page
title: linux/bootctl (English)
description: "Control EFI firmware boot settings and manage boot loader."
content_hash: 9f79d754e63364abf2eaf2762ce37da4a0adbd8f
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/bootctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/bootctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bootctl

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
