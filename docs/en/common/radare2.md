---
layout: page
title: common/radare2 (English)
description: "A set of reverse engineering tools."
content_hash: 07b5e00b3e6a800c1373aec0f89edc95d5b12586
last_modified_at: 2023-11-20
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

- Show help text for any command in the interactive CLI:

`> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">radare2_command</span>`?`

- Run a shell command from the interactive CLI:

`> !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_command</span>

- Dump raw bytes of current block to a file:

`> pr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bin</span>
