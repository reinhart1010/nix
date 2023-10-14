---
layout: page
title: linux/gzexe (English)
description: "Compress executable files while keeping them executable."
content_hash: 3d48fbd77a7cf72eef7677746fc4a3ff08f3ea78
last_modified_at: 2023-10-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gzexe

Compress executable files while keeping them executable.
Back up the original file, appending `~` to its name and create a shell script that uncompresses and executes the binary inside it.
More information: <https://manned.org/gzexe.1>.

- Compress an executable file in-place:

`gzexe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Decompress a compressed executable in-place (i.e. convert the shell script back to an uncompressed binary):

`gzexe -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_executable</span>
