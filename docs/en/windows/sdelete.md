---
layout: page
title: windows/sdelete (English)
description: "Securely delete file/directory from disk, or clean the free space on a volume/physical disk."
content_hash: 3f38daccfee025ab7e6f4cd7d65374d0225aa6c1
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# sdelete

Securely delete file/directory from disk, or clean the free space on a volume/physical disk.
More information: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- Delete files with 3 [p]asses:

`sdelete -p 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1 path\to\file2 ...</span>

- Delete folders and its [s]ubdirectories with 1 pass (default):

`sdelete -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory1 path\to\directory2 ...</span>

- Clean the free space of volume D: with 3 [p]asses:

`sdelete -p 3 D:`

- Clean the free space with [z]eros of physical disk 2, which should not contain any volumes to be cleaned:

`sdelete -z 2`
