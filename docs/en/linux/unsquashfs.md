---
layout: page
title: linux/unsquashfs (English)
description: "Uncompress, extract and list files in squashfs filesystems."
content_hash: 555d7163a8b4c03a6e3482bf69948afeb0aa2723
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/unsquashfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unsquashfs

Uncompress, extract and list files in squashfs filesystems.
More information: <https://manned.org/unsquashfs>.

- Extract a squashfs filesystem to `squashfs-root` in the current working directory:

`unsquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- Extract a squashfs filesystem to the specified directory:

`unsquashfs -dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- Display the names of files as they are extracted:

`unsquashfs -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- Display the names of files and their attributes as they are extracted:

`unsquashfs -linfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- List files inside the squashfs filesystem (without extracting):

`unsquashfs -ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>

- List files and their attributes inside the squashfs filesystem (without extracting):

`unsquashfs -lls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem.squashfs</span>
