---
layout: page
title: linux/findmnt (English)
description: "Find your filesystem."
content_hash: b46420a95ebc2a21abdba86aafb8743c96d05f20
last_modified_at: 2024-11-05
tldri18n_status: 2
---
# findmnt

Find your filesystem.
More information: <https://manned.org/findmnt>.

- List all mounted filesystems:

`findmnt`

- Search for a device:

`findmnt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Search for a mountpoint:

`findmnt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- Find filesystems in specific type:

`findmnt -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>

- Find filesystems with specific label:

`findmnt LABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BigStorage</span>

- Check mount table content in detail and verify `/etc/fstab`:

`findmnt --verify --verbose`
