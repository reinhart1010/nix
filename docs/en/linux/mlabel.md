---
layout: page
title: linux/mlabel (English)
description: "Set an MS-DOS volume label for FAT and VFAT filesystems."
content_hash: 1b1dc3cfc99de3b81e8e172453fe3856797017ec
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mlabel

Set an MS-DOS volume label for FAT and VFAT filesystems.
More information: <https://www.gnu.org/software/mtools/manual/mtools.html#mlabel>.

- Set a filesystem label:

`mlabel -i /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda</span>` ::"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_label</span>`"`
