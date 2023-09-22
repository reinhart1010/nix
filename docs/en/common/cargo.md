---
layout: page
title: common/cargo (English)
description: "Manage Rust projects and their module dependencies (crates)."
content_hash: 3a6dab702b8548873ced0ec11f7d5fcf0bcf2bdc
last_modified_at: 2023-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
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
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
---
# cargo

Manage Rust projects and their module dependencies (crates).
Some subcommands such as `build` have their own usage documentation.
More information: <https://doc.rust-lang.org/cargo>.

- Search for crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Install a binary crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate_name</span>

- List installed binary crates:

`cargo install --list`

- Create a new binary or library Rust project in the specified directory (or the current working directory by default):

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Add a dependency to `Cargo.toml` in the current directory:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Build the Rust project in the current directory using the release profile:

`cargo build --release`

- Build the Rust project in the current directory using the nightly compiler (requires `rustup`):

`cargo +nightly build`

- Build using a specific number of threads (default is the number of logical CPUs):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>
