---
layout: page
title: common/cargo-run (English)
description: "Run the current Cargo package."
content_hash: 85d00d5f04efb8fbb98abab4944b1ace05b397d0
last_modified_at: 2023-10-30
---
# cargo run

Run the current Cargo package.
Note: the working directory of the executed binary will be set to the current working directory.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Run the default binary target:

`cargo run`

- Run the specified binary:

`cargo run --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Run the specified example:

`cargo run --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Activate a space or comma separated list of features:

`cargo run --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature1 feature2 ...</span>

- Disable the default features:

`cargo run --no-default-features`

- Activate all available features:

`cargo run --all-features`

- Run with the given profile:

`cargo run --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
