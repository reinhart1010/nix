---
layout: page
title: linux/strip (English)
description: "Discard symbols from executables or object files."
content_hash: a5d3e728cf76f1b094801e0ca57f40252bc2c1d6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# strip

Discard symbols from executables or object files.
More information: <https://manned.org/strip>.

- Replace the input file with its stripped version:

`strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Strip symbols from a file, saving the output to a specific file:

`strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Strip debug symbols only:

`strip --strip-debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.o</span>
