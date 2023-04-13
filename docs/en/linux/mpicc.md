---
layout: page
title: linux/mpicc (English)
description: "Open MPI C wrapper compiler."
content_hash: bc44f1e529526a7e6313aa0eb856de3233ce1aa2
last_modified_at: 2023-04-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mpicc

Open MPI C wrapper compiler.
The wrappers are simply thin shells on top of a C compiler, they add the relevant compiler and linker flags to the command line that are necessary to compile/link Open MPI programs, and then invoke the underlying C compiler to actually perform the command.
More information: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compile a source code file into an object file:

`mpicc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>

- Link an object file and make an executable:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/object_file.o</span>

- Compile and link source code in a single command:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.c</span>
