---
layout: page
title: common/cargo-test (English)
description: "Execute the unit and integration tests of a Rust package."
content_hash: 29af1e9bbb539db5ec56abc64c4e30da292f2d6d
---
# cargo test

Execute the unit and integration tests of a Rust package.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Only run tests containing a specific string in their names:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testname</span>

- Set the number of simultaneous running test cases:

`cargo test -- --test-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Require that `Cargo.lock` is up to date:

`cargo test --locked`

- Test artifacts in release mode, with optimizations:

`cargo test --release`

- Test all packages in the workspace:

`cargo test --workspace`

- Run tests for a package:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Run tests without hiding output from test executions:

`cargo test -- --nocapture`
