---
layout: page
title: common/glab-alias (English)
description: "Manage GitLab CLI command aliases."
content_hash: 23d1aeea05a674e6a8f0e6c7ecefc272d2d785a0
last_modified_at: 2023-07-16
---
# glab alias

Manage GitLab CLI command aliases.
More information: <https://glab.readthedocs.io/en/latest/alias>.

- Display the subcommand help:

`glab alias`

- List all the aliases `glab` is configured to use:

`glab alias list`

- Create a `glab` subcommand alias:

`glab alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mrv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr view</span>`'`

- Set a shell command as a `glab` subcommand:

`glab alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Delete a command shortcut:

`glab alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>
