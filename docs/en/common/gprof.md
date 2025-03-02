---
layout: page
title: common/gprof (English)
description: "Performance analysis tool for many programming languages."
content_hash: 166694f839d112370bcbda41e1f40bf0a2401e80
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/gprof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gprof

Performance analysis tool for many programming languages.
It profiles the function executions of a program.
More information: <https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>.

- Compile binary to default `a.out` with gprof information and run it to get `gmon.out`:

`gcc -pg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.c</span>` && ./a.out`

- Run gprof on default `a.out` and `gmon.out` to obtain profile output:

`gprof`

- Run gprof on a named binary:

`gprof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/gmon.out</span>

- Suppress profile field's description:

`gprof -b`

- Display routines that have zero usage:

`gprof -bz`
