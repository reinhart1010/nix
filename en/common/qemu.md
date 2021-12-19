---
layout: page
title: common/qemu (English)
description: "Generic machine emulator and virtualizer."
content_hash: c9667f46a29b736f15ea45d83427115387730855
---
# qemu

Generic machine emulator and virtualizer.
Supports a large variety of CPU architectures.
More information: <https://www.qemu.org>.

- Boot from image emulating i386 architecture:

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>

- Boot from image emulating x64 architecture:

`qemu-system-x86_64 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>

- Boot QEMU instance with a live ISO image:

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_image.iso</span>` -boot d`

- Specify amount of RAM for instance:

`qemu-system-i386 -m 256 -hda image_name.img -cdrom os-image.iso -boot d`

- Boot from physical device (e.g. from USB to test bootable medium):

`qemu-system-i386 -hda /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_device</span>
