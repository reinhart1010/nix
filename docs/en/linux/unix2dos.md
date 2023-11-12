---
layout: page
title: linux/unix2dos (English)
description: "Change Unix-style line endings to DOS-style."
content_hash: 393488d6b65fbe7d981875c5037625b0bf22adc8
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2dos

Change Unix-style line endings to DOS-style.
Replaces LF with CRLF.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with DOS-style line endings:

`unix2dos -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/unix_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dos_file</span>
