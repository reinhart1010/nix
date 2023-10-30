---
layout: page
title: common/cargo-logout (English)
description: "Remove an API token from the registry locally."
content_hash: 28b36ae9432c7e1e64362ac4221d2515d43d5595
last_modified_at: 2023-10-30
---
# cargo logout

Remove an API token from the registry locally.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove the API token from the local credential storage:

`cargo logout`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo logout --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
