---
layout: page
title: common/gprof (English)
description: "Performance analysis tool for many programming languages."
content_hash: ff61d481614591ad001f7fad74934d4ad4f177bf
---
# gprof

Performance analysis tool for many programming languages.
It profiles the function executions of a program.
More information: <https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>.

- Compile binary with gprof information and run it to get `gmon.out`:

`gcc -pg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.c</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./a.out</span>

- Run gprof to obtain profile output:

`gprof`

- Suppress profile field's description:

`gprof -b`

- Display routines that have zero usage:

`gprof -bz`
