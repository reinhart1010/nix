---
layout: page
title: linux/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 9828a6775e604a5c7908651f2106cf3b7fd96756
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# df

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
