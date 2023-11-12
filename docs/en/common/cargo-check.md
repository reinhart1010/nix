---
layout: page
title: common/cargo-check (English)
description: "Check a local package and all of its dependencies for errors."
content_hash: 5af721d27ae9090844dd9000e98ed902afe13b3b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cargo check

Check a local package and all of its dependencies for errors.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- Check the current package:

`cargo check`

- Check all tests:

`cargo check --tests`

- Check the integration tests in `tests/integration_test1.rs`:

`cargo check --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_test1</span>

- Check the current package with the features `feature1` and `feature2`:

`cargo check --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature1,feature2</span>

- Check the current package with default features disabled:

`cargo check --no-default-features`
