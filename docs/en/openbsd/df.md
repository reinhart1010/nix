---
layout: page
title: openbsd/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 2ec7110e99179c49612892691c41f36097b70d02
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# df

Display an overview of the filesystem disk space usage.
More information: <https://man.openbsd.org/df.1>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Display all filesystems and their disk usage in human-readable form (based on powers of 1024):

`df -h`

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Include statistics on the number of free and used [i]nodes:

`df -i`

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a portable way:

`df -P`
