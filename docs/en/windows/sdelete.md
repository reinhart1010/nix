---
layout: page
title: windows/sdelete (English)
description: "Securely delete file/directory from disk, or clean the free space on a volume/physical disk."
content_hash: 3f38daccfee025ab7e6f4cd7d65374d0225aa6c1
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/sdelete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdelete

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
