---
layout: page
title: common/cargo-owner (English)
description: "Manage the owners of a crate on the registry."
content_hash: e0a6d446a882942ab4d276a0d30e921d1f6998a6
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# cargo owner

Manage the owners of a crate on the registry.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- Invite the given user or team as an owner:

`cargo owner --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|github:org_name:team_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>

- Remove the given user or team as an owner:

`cargo owner --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|github:org_name:team_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>

- List owners of a crate:

`cargo owner --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate</span>

- Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>):

`cargo owner --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
