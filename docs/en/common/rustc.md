---
layout: page
title: common/rustc (English)
description: "The Rust compiler."
content_hash: 6fca564556b72182165c506dadc377ef3b4a8400
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustc

The Rust compiler.
Rust projects usually use `cargo` instead of invoking `rustc` directly.
More information: <https://doc.rust-lang.org/rustc>.

- Compile a binary crate:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.rs</span>

- Compile with optimizations (`s` means optimize for binary size; `z` is the same with even more optimizations):

`rustc -C lto -C opt-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|s|z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.rs</span>

- Compile with debugging information:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.rs</span>

- Explain an error message:

`rustc --explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error_code</span>

- Compile with architecture-specific optimizations for the current CPU:

`rustc -C target-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">native</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.rs</span>

- Display the target list (Note: you have to add a target using `rustup` first to be able to compile for it):

`rustc --print target-list`

- Compile for a specific target:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triple</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.rs</span>
