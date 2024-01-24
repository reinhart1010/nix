---
layout: page
title: common/cargo-login (English)
description: "Save an API token from the registry locally."
content_hash: 0a0ba4621c7b0145d7a075edec43f0d69cd9255d
last_modified_at: 2024-01-24
tldri18n_status: 2
---
# cargo login

Save an API token from the registry locally.
The token is used to authenticate to a package registry. You can remove it using `cargo logout`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

- Add an API token to the local credential storage (located in `$CARGO_HOME/credentials.toml`):

`cargo login`

- Use the specified registry (registry names can be defined in the config - the default is <https://crates.io>):

`cargo login --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
