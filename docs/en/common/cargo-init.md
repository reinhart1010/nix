---
layout: page
title: common/cargo-init (English)
description: "Create a new Cargo package."
content_hash: 7e3e0698e1e1882ea9bdaa29788870ac85fe15da
last_modified_at: 2024-03-20
related_topics:
  - title: 中文 version
    url: /zh/common/cargo-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo init

Create a new Cargo package.
Equivalent of `cargo new`, but specifying a directory is optional.
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
