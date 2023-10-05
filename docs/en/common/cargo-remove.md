---
layout: page
title: common/cargo-remove (English)
description: "Remove dependencies from a `Cargo.toml` manifest file."
content_hash: b448f37dd418fc4c296944834e7934f0f33524a7
last_modified_at: 2023-10-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo remove

Remove dependencies from a `Cargo.toml` manifest file.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove one or more dependencies from the `Cargo.toml` manifest:

`cargo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Remove a build dependency:

`cargo remove --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Remove a dependency to the given target platform:

`cargo remove --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` {dependency_name</span>

- Don't actually write to the manifest:

`cargo remove --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Display verbose output:

`cargo remove --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Do not print Cargo log message:

`cargo remove --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Specify package to remove from:

`cargo remove --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">specification</span>` {dependency_name</span>

- Display help:

`cargo remove --help`
