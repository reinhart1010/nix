---
layout: page
title: linux/unix2dos (English)
description: "Change Unix-style line endings to DOS-style."
content_hash: 7fa4924d3345845655e0c6ebdc726a59e25e9033
last_modified_at: 2024-09-27
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2dos

Change Unix-style line endings to DOS-style.
Replaces LF with CRLF.
See also `unix2mac`, `dos2unix`, and `mac2unix`.
More information: <https://manned.org/unix2dos>.

- Change the line endings of a file:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with DOS-style line endings:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_file</span>

- Display file information:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Keep/add/remove Byte Order Mark:

`unix2dos --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
