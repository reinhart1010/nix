---
layout: page
title: linux/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 9828a6775e604a5c7908651f2106cf3b7fd96756
last_modified_at: 2024-01-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

Display an overview of the filesystem disk space usage.
More information: <https://www.gnu.org/software/coreutils/df>.

- Display all filesystems and their disk usage:

`df`

- Display all filesystems and their disk usage in human-readable form:

`df -h`

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Include statistics on the number of free inodes:

`df -i`

- Display filesystems but exclude the specified types:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
