---
layout: page
title: freebsd/df (English)
description: "Display an overview of the filesystem disk space usage."
content_hash: 78a6d79d894a76acd4433f8c776e26cc8cca953c
last_modified_at: 2024-01-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

Display an overview of the filesystem disk space usage.
More information: <https://man.freebsd.org/cgi/man.cgi?df>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Use [h]uman-readable units (based on powers of 1024) and display a grand total:

`df -h -c`

- Use [H]uman-readable units (based on powers of 1000):

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- Display the filesystem and its disk usage containing the given file or directory:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Include statistics on the number of free and used [i]nodes including the filesystem [T]ypes:

`df -iT`

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a [P]ortable way:

`df -P`
