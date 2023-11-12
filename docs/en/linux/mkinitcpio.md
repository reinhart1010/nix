---
layout: page
title: linux/mkinitcpio (English)
description: "Generates initial ramdisk environments for booting the Linux kernel based on the specified preset(s)."
content_hash: d67f64f9743332d62970350b2fdfc1fe80238eca
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mkinitcpio

Generates initial ramdisk environments for booting the Linux kernel based on the specified preset(s).
More information: <https://man.archlinux.org/man/mkinitcpio.8>.

- Perform a dry run (print what would be done without actually doing it):

`mkinitcpio`

- Generate a ramdisk environment based on the `linux` preset:

`mkinitcpio --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>

- Generate a ramdisk environment based on the `linux-lts` preset:

`mkinitcpio --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux-lts</span>

- Generate ramdisk environments based on all existing presets (used to regenerate all the initramfs images after a change in `/etc/mkinitcpio.conf`):

`mkinitcpio --allpresets`

- Generate an initramfs image using an alternative configuration file:

`mkinitcpio --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mkinitcpio.conf</span>` --generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initramfs.img</span>

- Generate an initramfs image for a kernel other than the one currently running (the installed kernel releases can be found in `/usr/lib/modules/`):

`mkinitcpio --kernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_version</span>` --generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initramfs.img</span>

- List all available hooks:

`mkinitcpio --listhooks`

- Display help for a specific hook:

`mkinitcpio --hookhelp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hook_name</span>
