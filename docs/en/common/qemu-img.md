---
layout: page
title: common/qemu-img (English)
description: "Create and manipulate Quick Emulator Virtual HDD images."
content_hash: 1f04681faa54c31f72819db0df8a15eeacfff6e7
last_modified_at: 2024-05-23
tldri18n_status: 2
---
# qemu-img

Create and manipulate Quick Emulator Virtual HDD images.
More information: <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- Create disk image with a specific size (in gigabytes):

`qemu-img create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gigabytes</span>`G`

- Show information about a disk image:

`qemu-img info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>

- Increase or decrease image size:

`qemu-img resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gigabytes</span>`G`

- Dump the allocation state of every sector of the specified disk image:

`qemu-img map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name.img</span>

- Convert a VMware .vmdk disk image to a KVM .qcow2 disk image:

`qemu-img convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vmdk</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file/foo.vmdk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file/foo.qcow2</span>
