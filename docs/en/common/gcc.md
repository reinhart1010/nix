---
layout: page
title: common/gcc (English)
description: "Preprocess and compile C and C++ source files, then assemble and link them together."
content_hash: 5105b93dec14f869af38c31dde02a34c82627018
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gcc.html
    icon: bi bi-globe
---
# gcc

Preprocess and compile C and C++ source files, then assemble and link them together.
More information: <https://gcc.gnu.org>.

- Compile multiple source files into executable:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source1.c path/to/source2.c ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Allow warnings, debug symbols in output:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` -Wall -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Include libraries from a different path:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/header</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_name</span>

- Compile source code into Assembler instructions:

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>

- Compile source code into an object file without linking:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>
