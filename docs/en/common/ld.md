---
layout: page
title: common/ld (English)
description: "Link object files together."
content_hash: 07ee2f1a3a317bdafb43a4898742449a29ad7f20
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/ld.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ld

Link object files together.
More information: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- Link a specific object file with no dependencies into an executable:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Link two object files together:

`ld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.o</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Dynamically link an x86_64 program to glibc (file paths change depending on the system):

`ld --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>` --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>` /lib/crtn.o`
