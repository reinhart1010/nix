---
layout: page
title: common/glab-alias (English)
description: "Manage GitLab CLI command aliases from the command-line."
content_hash: b5feacc49f4ded6b61df5d87f56acbbdfecb4b73
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab alias

Manage GitLab CLI command aliases from the command-line.
More information: <https://glab.readthedocs.io/en/latest/alias>.

- Display the subcommand help:

`glab alias`

- List all the aliases `glab` is configured to use:

`glab alias list`

- Create a `glab` subcommand alias:

`glab alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr view</span>`'`

- Set a shell command as a `glab` subcommand:

`glab alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Delete a command shortcut:

`glab alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>
