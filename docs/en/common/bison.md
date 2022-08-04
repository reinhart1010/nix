---
layout: page
title: common/bison (English)
description: "GNU parser generator."
content_hash: f42673820015a75c5f6ba795f69e92cad1089c32
---
# bison

GNU parser generator.
More information: <https://www.gnu.org/software/bison/>.

- Compile a bison definition file:

`bison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Compile in debug mode, which causes the resulting parser to write additional information to the standard output:

`bison --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Specify the output filename:

`bison --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.y</span>

- Be verbose when compiling:

`bison --verbose`
