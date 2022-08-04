---
layout: page
title: common/gh-codespace (English)
description: "Connect and manage your codespaces in GitHub."
content_hash: d76e79b9b0d842d33310c2523e1143414bb524a7
---
# gh codespace

Connect and manage your codespaces in GitHub.
More information: <https://cli.github.com/manual/gh_codespace>.

- Create a codespace in GitHub interactively:

`gh codespace create`

- List all available codespaces:

`gh codespace list`

- Connect to a codespace via SSH interactively:

`gh codespace ssh`

- Transfer a file to a codespace interactively:

`gh codespace cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file</span>` remote:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_file</span>

- List the ports of a codespace interactively:

`gh codespace ports`

- Print the logs from a codespace interactively:

`gh codespace logs`

- Delete a codespace interactively:

`gh codespace delete`

- Display help for a subcommand:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
