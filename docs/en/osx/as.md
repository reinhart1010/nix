---
layout: page
title: osx/as (English)
description: "Portable GNU assembler."
content_hash: ee1dcb0e71914c1d59a7abe8fdda6bd4a42ec783
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Portable GNU assembler.
Primarily intended to assemble output from `gcc` to be used by `ld`.
More information: <https://www.unix.com/man-page/osx/1/as/>.

- Assemble a file, writing the output to `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.s</span>

- Assemble the output to a given file:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.o</span>

- Generate output faster by skipping whitespace and comment preprocessing. (Should only be used for trusted compilers):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.s</span>

- Include a given path to the list of directories to search for files specified in `.include` directives:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.s</span>
