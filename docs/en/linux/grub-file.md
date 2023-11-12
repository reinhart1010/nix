---
layout: page
title: linux/grub-file (English)
description: "Check if a file is of a specific bootable image type."
content_hash: 603383e7ff8b315c095b57df55b7068bc9bd5062
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# grub-file

Check if a file is of a specific bootable image type.
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

- Check if a file is an x86_64 XNU image (Mac OS X kernel):

`grub-file --is-x86_64-xnu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
