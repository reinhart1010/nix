---
layout: page
title: linux/gcov (English)
description: "Code coverage analysis and profiling tool that discovers untested parts of a program."
content_hash: 2fba2131283261dc764116334e9276915716f52a
---
# gcov

Code coverage analysis and profiling tool that discovers untested parts of a program.
Also displays a copy of source code annotated with execution frequencies of code segments.
More information: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>.

- Generate a coverage report named `file.cpp.gcov`:

`gcov `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Write individual execution counts for every basic block:

`gcov --all-blocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Write branch frequencies to the output file and print summary information to stdout as a percentage:

`gcov --branch-probabilities `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Write branch frequencies as the number of branches taken, rather than the percentage:

`gcov --branch-counts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Do not create a `gcov` output file:

`gcov --no-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Write file level as well as function level summaries:

`gcov --function-summaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>
