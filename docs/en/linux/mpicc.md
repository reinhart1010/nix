---
layout: page
title: linux/mpicc (English)
description: "Open MPI C wrapper compiler."
content_hash: 19cbce4c580bf36a8bd5f9542e77def3f5888c34
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/mpicc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpicc

Open MPI C wrapper compiler.
The wrappers are simply thin shells on top of a C compiler, they add the relevant compiler and linker flags to the command-line that are necessary to compile/link Open MPI programs, and then invoke the underlying C compiler to actually perform the command.
More information: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compile a source code file into an object file:

`mpicc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>

- Link an object file and make an executable:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/object_file.o</span>

- Compile and link source code in a single command:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>
