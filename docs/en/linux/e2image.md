---
layout: page
title: linux/e2image (English)
description: "Save critical ext2/ext3/ext4 filesystem metadata to a file."
content_hash: bcdf41bf33bb34de05518b9d27aff37dc4613825
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# e2image

Save critical ext2/ext3/ext4 filesystem metadata to a file.
More information: <https://manned.org/e2image>.

- Write metadata located on device to a specific file:

`e2image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Print metadata located on device to `stdout`:

`e2image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` -`

- Restore the filesystem metadata back to the device:

`e2image -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Create a large raw sparse file with metadata at proper offsets:

`e2image -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Create a QCOW2 image file instead of a normal or raw image file:

`e2image -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>
