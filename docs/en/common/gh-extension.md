---
layout: page
title: common/gh-extension (English)
description: "Manage extensions for the GitHub CLI."
content_hash: c46fb3c1666ae5a7697bb7fe1427ab02fbdab3d7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gh extension

Manage extensions for the GitHub CLI.
More information: <https://cli.github.com/manual/gh_extension>.

- Initialize a new GitHub CLI extension project in a directory of the same name:

`gh extension create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_name</span>

- Install an extension from a GitHub repository:

`gh extension install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- List installed extensions:

`gh extension list`

- Upgrade a specific extension:

`gh extension upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_name</span>

- Upgrade all extensions:

`gh extension upgrade --all`

- List installed extensions:

`gh extension list`

- Remove an extension:

`gh extension remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_name</span>

- Display help about a subcommand:

`gh extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
