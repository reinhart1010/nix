---
layout: page
title: common/cargo (English)
description: "Manage Rust projects and their module dependencies (crates)."
content_hash: 05dd21e3fc2a3c7d28ef1753974623f31fc6cec0
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
---
# cargo

Manage Rust projects and their module dependencies (crates).
Some subcommands such as `cargo build` have their own usage documentation.
More information: <https://crates.io/>.

- Search for crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Install a crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate_name</span>

- List installed crates:

`cargo install --list`

- Create a new binary or library Rust project in the current directory:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Create a new binary or library Rust project in the specified directory:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Build the Rust project in the current directory:

`cargo build`

- Build using a specific number of threads (default is the number of CPU cores):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>
