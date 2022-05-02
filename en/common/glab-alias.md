---
layout: page
title: common/glab-alias (English)
description: "Manage GitLab CLI command aliases from the command-line."
content_hash: 44bcf69dfb900db8e42bf215498613c53d978d30
---
# glab alias

Manage GitLab CLI command aliases from the command-line.
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
