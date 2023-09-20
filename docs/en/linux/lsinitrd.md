---
layout: page
title: linux/lsinitrd (English)
description: "Show the contents of an initramfs image."
content_hash: 91bcf29ce54b9c0d8eafc368ee6ae69533722d02
last_modified_at: 2023-09-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsinitrd

Show the contents of an initramfs image.
See also: `dracut`.
More information: <https://github.com/dracutdevs/dracut/blob/master/man/lsinitrd.1.asc>.

- Show the contents of the initramfs image for the current kernel:

`lsinitrd`

- Show the contents of the initramfs image for the specified kernel:

`lsinitrd --kver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_version</span>

- Show the contents of the specified initramfs image:

`lsinitrd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initramfs.img</span>

- List modules included in the initramfs image:

`lsinitrd --mod`

- Unpack the initramfs to the current directory:

`lsinitrd --unpack`
