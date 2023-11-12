---
layout: page
title: common/gfortran (English)
description: "Preprocess and compile Fortran source files, then assemble and link them together."
content_hash: d0ffd9e0bfbb467cc71e01388180e4dea10c928e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gfortran

Preprocess and compile Fortran source files, then assemble and link them together.
More information: <https://gcc.gnu.org/wiki/GFortran>.

- Compile multiple source files into an executable:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source1.f90 path/to/source2.f90 ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Show common warnings, debug symbols in output, and optimize without affecting debugging:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.f90</span>` -Wall -g -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Include libraries from a different path:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.f90</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mod_and_include</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library_name</span>

- Compile source code into Assembler instructions:

`gfortran -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.f90</span>

- Compile source code into an object file without linking:

`gfortran -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.f90</span>
