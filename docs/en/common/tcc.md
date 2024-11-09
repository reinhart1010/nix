---
layout: page
title: common/tcc (English)
description: "A tiny C compiler that can run C source files as scripts and otherwise has command-line options similar to `gcc`."
content_hash: 0a71fcf99d069fb87862a3f77c81e52e44b9eb75
last_modified_at: 2024-11-09
tldri18n_status: 2
---
# tcc

A tiny C compiler that can run C source files as scripts and otherwise has command-line options similar to `gcc`.
More information: <https://bellard.org/tcc/tcc-doc.html>.

- Compile and link 2 source files to generate an executable:

`tcc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.c</span>

- Directly run an input file like a script and pass arguments to it:

`tcc -run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Interpret C source files with a shebang inside the file:

`#!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/full/path/to/tcc</span>` -run`
