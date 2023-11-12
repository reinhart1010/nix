---
layout: page
title: common/mcfly (English)
description: "A smart command history search and management tool."
content_hash: 760c1d2be04ef5f19b6969985bf5dec5fc3745cd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mcfly

A smart command history search and management tool.
Replaces your default shell history search (ctrl-r) with an intelligent search engine providing context and relevance to the commands.
More information: <https://github.com/cantino/mcfly>.

- Print the mcfly integration code for the specified shell:

`mcfly init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>

- Search the history for a command, with 20 results:

`mcfly search --results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>`"`

- Add a new command to the history:

`mcfly add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Record that a directory has moved and transfer the historical records from the old path to the new one:

`mcfly move "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/old_directory</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_directory</span>`"`

- Train the suggestion engine (developer tool):

`mcfly train`

- Display help for a specific subcommand:

`mcfly help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
