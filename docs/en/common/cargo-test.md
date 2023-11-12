---
layout: page
title: common/cargo-test (English)
description: "Execute the unit and integration tests of a Rust package."
content_hash: 8d0becd90c2a7095bbd4215c782061d4142804f8
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-test.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo test

Execute the unit and integration tests of a Rust package.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Only run tests containing a specific string in their names:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testname</span>

- Set the number of simultaneous running test cases:

`cargo test -- --test-threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Test artifacts in release mode, with optimizations:

`cargo test --release`

- Test all packages in the workspace:

`cargo test --workspace`

- Run tests for a specific package:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Run tests without hiding output from test executions:

`cargo test -- --nocapture`
