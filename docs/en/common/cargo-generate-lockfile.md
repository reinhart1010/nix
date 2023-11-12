---
layout: page
title: common/cargo-generate-lockfile (English)
description: "Generate the `Cargo.lock` file for the current package. Similar to `cargo update`, but has less options."
content_hash: 608307e9c62d5b680f85d6777daac8aef9b94f64
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cargo generate-lockfile

Generate the `Cargo.lock` file for the current package. Similar to `cargo update`, but has less options.
If the lockfile already exists it will be rebuilt with latest version of every package.
More information: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- Generate a `Cargo.lock` file with the latest version of every package:

`cargo generate-lockfile`
