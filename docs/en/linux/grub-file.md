---
layout: page
title: linux/grub-file (English)
description: "Check if a file is of a bootable image type."
content_hash: f988d780d9a7bda0eb406a2ef5ca7ec464b20bcc
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# grub-file

Check if a file is of a bootable image type.
More information: <https://manned.org/grub-file>.

- Check if a file is an ARM EFI image:

`grub-file --is-arm-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a file is an i386 EFI image:

`grub-file --is-i386-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a file is an x86_64 EFI image:

`grub-file --is-x86_64-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a file is an ARM image (Linux kernel):

`grub-file --is-arm-linux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a file is an x86 image (Linux kernel):

`grub-file --is-x86-linux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if a file is an x86_64 XNU image (macOS kernel):

`grub-file --is-x86_64-xnu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
