---
layout: page
title: linux/ausyscall (English)
description: "Program that allows mapping syscall names and numbers."
content_hash: 2918c92c35c7fb766866506b136206a2fc6e01b8
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ausyscall

Program that allows mapping syscall names and numbers.
More information: <https://manned.org/ausyscall>.

- Display syscall number of a specific system call:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Display name of a specific system call number:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call_number</span>

- Display all system calls for a specific architecture:

`ausyscall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>` --dump`
