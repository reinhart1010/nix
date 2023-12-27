---
layout: page
title: common/radare2 (English)
description: "A set of reverse engineering tools."
content_hash: d05c2380b69257107a3f619c3b699ff52ef7e6f8
last_modified_at: 2023-12-27
related_topics:
  - title: Nederlands version
    url: /nl/common/radare2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radare2

A set of reverse engineering tools.
More information: <https://www.radare.org/r/docs.html>.

- Open a file in write mode without parsing the file format headers:

`radare2 -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Debug a program:

`radare2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Run a script before entering the interactive CLI:

`radare2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.r2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Display help text for any command in the interactive CLI:

`> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">radare2_command</span>`?`

- Run a shell command from the interactive CLI:

`> !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_command</span>

- Dump raw bytes of current block to a file:

`> pr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bin</span>
