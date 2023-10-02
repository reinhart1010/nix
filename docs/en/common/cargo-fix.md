---
layout: page
title: common/cargo-fix (English)
description: "Automatically fix lint warnings reported by `rustc`."
content_hash: 582d670b264f83a51ab04d01ece848b01a82fbad
last_modified_at: 2023-10-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo fix

Automatically fix lint warnings reported by `rustc`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- Fix code even if it already has compiler errors:

`cargo fix --broken-code`

- Fix code even if the working directory has changes:

`cargo fix --allow-dirty`

- Fix the package’s library:

`cargo fix --lib`

- Fix the specified integration test:

`cargo fix --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Fix all members in the workspace:

`cargo fix --workspace`

- Set the directory for all generated artifacts and intermediate files:

`cargo fix --target-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Restrict Cargo from access to network for any reason:

`cargo fix --offline`

- Run `n` jobs in parallel (default: number of logical CPUs):

`cargo fix --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
