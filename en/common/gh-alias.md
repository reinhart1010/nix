---
layout: page
title: common/gh-alias (English)
description: "Manage GitHub CLI command aliases from the command-line."
content_hash: 2cc9b06e1739e769d41774a52931440edfef07dd
---
# gh alias

Manage GitHub CLI command aliases from the command-line.
More information: <https://cli.github.com/manual/gh_alias>.

- Display the subcommand help:

`gh alias`

- List all the aliases `gh` is configured to use:

`gh alias list`

- Create a `gh` subcommand alias:

`gh alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr view</span>`'`

- Set a shell command as a `gh` subcommand:

`gh alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Delete a command shortcut:

`gh alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>
