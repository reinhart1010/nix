---
layout: page
title: common/cargo-run (English)
description: "Run the current Cargo package."
content_hash: 123db3f76acb282cbd4aeb9af2530f6f3ea58cd1
last_modified_at: 2023-10-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo run

Run the current Cargo package.
Note: Set the working directory of the binary executed to the current working directory.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Run the default binary target:

`cargo run`

- Run the specified binary:

`cargo run --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Run the specified example:

`cargo run --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Activate a space or comma separated list of features:

`cargo run --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature1 feature2 ...</span>

- Disable the default feature:

`cargo run --no-default-features`

- Activate all available features:

`cargo run --all-features`

- Run with the given profile:

`cargo run --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
