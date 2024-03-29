---
layout: page
title: linux/resize2fs (English)
description: "Resize an ext2, ext3 or ext4 filesystem."
content_hash: 47aeda876e7c8e49fdf5167031e65247b1e12876
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# resize2fs

Resize an ext2, ext3 or ext4 filesystem.
Does not resize the underlying partition. The filesystem may have to be unmounted first, read the man page for more details.
More information: <https://manned.org/resize2fs>.

- Automatically resize a filesystem:

`resize2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Resize the filesystem to a size of 40G, displaying a progress bar:

`resize2fs -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>

- Shrink the filesystem to its minimum possible size:

`resize2fs -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
