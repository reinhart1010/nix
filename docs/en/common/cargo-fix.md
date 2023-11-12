---
layout: page
title: common/cargo-fix (English)
description: "Automatically fix lint warnings reported by `rustc`."
content_hash: 201663619e51377cc28f791c67a418bdb101d2d0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cargo fix

Automatically fix lint warnings reported by `rustc`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- Fix code even if it already has compiler errors:

`cargo fix --broken-code`

- Fix code even if the working directory has changes:

`cargo fix --allow-dirty`

- Migrate a package to the next Rust edition:

`cargo fix --edition`

- Fix the package’s library:

`cargo fix --lib`

- Fix the specified integration test:

`cargo fix --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Fix all members in the workspace:

`cargo fix --workspace`
