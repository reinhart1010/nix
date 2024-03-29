---
layout: page
title: common/cargo-logout (English)
description: "Remove an API token from the registry locally."
content_hash: e8cb56190bc5dc5d1db67e3baf4bc63f22730c78
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# cargo logout

Remove an API token from the registry locally.
The token is used to authenticate to a package registry. You can add it back using `cargo login`.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove an API token from the local credential storage (located in `$CARGO_HOME/credentials.toml`):

`cargo logout`

- Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>):

`cargo logout --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
