---
layout: page
title: common/rustc (English)
description: "The Rust compiler."
content_hash: a9711567f1e7467b191bce4139ce6ec844e7812e
last_modified_at: 2023-01-04
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/rustc.html
    icon: bi bi-globe
---
# rustc

The Rust compiler.
Processes, compiles and links Rust language source files.
More information: <https://doc.rust-lang.org/rustc>.

- Compile a single file:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rs</span>

- Compile with high optimization:

`rustc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rs</span>

- Compile with debugging information:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rs</span>

- Compile with architecture-specific optimizations for the current CPU:

`rustc -C target-cpu=native `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rs</span>

- Display architecture-specific optimizations for the current CPU:

`rustc -C target-cpu=native --print cfg`

- Display target list:

`rustc --print target-list`

- Compile for a specific target:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triple</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rs</span>
