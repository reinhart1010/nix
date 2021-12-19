---
layout: page
title: common/bootctl (English)
description: "Control EFI firmware boot settings and manage boot loader."
content_hash: e620b88f3f461c78100a0b8f8f2b433e5a8f5e31
---
# bootctl

Control EFI firmware boot settings and manage boot loader.
More information: <https://man.archlinux.org/man/bootctl.1>.

- Show information about the system firmware and the bootloaders:

`sudo bootctl status`

- Set a flag to boot into the system firmware on the next boot (similar to `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Specify the path to the EFI system partition (defaults to `/efi/`, `/boot/` or `/boot/efi`):

`sudo bootctl --esp-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/efi_system_partition/</span>

- Show all available bootloader entries:

`sudo bootctl list`

- Install `systemd-boot` into the EFI system partition:

`sudo bootctl install`

- Remove all installed versions of `systemd-boot` from the EFI system partition:

`sudo bootctl remove`
