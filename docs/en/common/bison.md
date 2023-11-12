---
layout: page
title: common/bison (English)
description: "GNU parser generator."
content_hash: 671a201c24d572499face01e821e10af9ff05113
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# bison

GNU parser generator.
More information: <https://www.gnu.org/software/bison/>.

- Compile a bison definition file:

`bison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Compile in debug mode, which causes the resulting parser to write additional information to `stdout`:

`bison --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Specify the output filename:

`bison --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Be verbose when compiling:

`bison --verbose`
