---
layout: page
title: common/swc (English)
description: "JavaScript and TypeScript compiler written in Rust."
content_hash: 3f14b86599074592bbe4d085cb2ce7dc01753d0a
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# swc

JavaScript and TypeScript compiler written in Rust.
More information: <https://swc.rs>.

- Transpile a specified input file and output to `stdout`:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Transpile the input file every time it is changed:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --watch`

- Transpile a specified input file and output to a specific file:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Transpile a specified input directory and output to a specific directory:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>

- Transpile a specified input directory using a specific configuration file:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.swcrc</span>

- Ignore files in a directory specified using glob path:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ignored_file1 path/to/ignored_file2 ...</span>
