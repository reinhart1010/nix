---
layout: page
title: common/gh-alias (English)
description: "Manage GitHub CLI command aliases."
content_hash: 33ed7ece586825491f2a8c9097623793dc999695
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/common/gh-alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh alias

Manage GitHub CLI command aliases.
More information: <https://cli.github.com/manual/gh_alias>.

- List all the aliases `gh` is configured to use:

`gh alias list`

- Create a `gh` subcommand alias:

`gh alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pv</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr view</span>`'`

- Set a shell command as a `gh` subcommand:

`gh alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Delete a command shortcut:

`gh alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>

- Display the subcommand help:

`gh alias`
