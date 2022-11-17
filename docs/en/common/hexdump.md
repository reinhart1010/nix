---
layout: page
title: common/hexdump (English)
description: "An ASCII, decimal, hexadecimal, octal dump."
content_hash: b42e7cc182582154dd3b4877796b50925195046a
related_topics:
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
---
# hexdump

An ASCII, decimal, hexadecimal, octal dump.
More information: <https://manned.org/hexdump>.

- Print the hexadecimal representation of a file, replacing duplicate lines by '*':

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the input offset in hexadecimal and its ASCII representation in two columns:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the hexadecimal representation of a file, but interpret only n bytes of the input:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Don't replace duplicate lines with '*':

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
