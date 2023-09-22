---
layout: page
title: common/cargo-init (English)
description: "Create a new Cargo package."
content_hash: 220036df4da0f154f5abb18d55213e60ab1892f5
last_modified_at: 2023-09-22
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo init

Create a new Cargo package.
Equivalent of `cargo new`, but specifiying a directory is optional.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Initialize a Rust project with a binary target in the current directory:

`cargo init`

- Initialize a Rust project with a binary target in the specified directory:

`cargo init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a Rust project with a library target in the current directory:

`cargo init --lib`

- Initialize a version control system repository in the project directory (default: `git`):

`cargo init --vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg|pijul|fossil|none</span>

- Set the package name (default: directory name):

`cargo init --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
