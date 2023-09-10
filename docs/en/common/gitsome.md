---
layout: page
title: common/gitsome (English)
description: "A terminal-based interface for GitHub, accessed via the `gh` command."
content_hash: af4c3dbf9b116474c65434417c9a0f86dd28b3b3
last_modified_at: 2023-09-10
related_topics:
  - title: Türkçe version
    url: /tr/common/gitsome.html
    icon: bi bi-globe
---
# gitsome

A terminal-based interface for GitHub, accessed via the `gh` command.
It also provides menu-style autocomplete suggestions for `git` commands.
More information: <https://github.com/donnemartin/gitsome>.

- Enter the gitsome shell (optional), to enable autocompletion and interactive help for Git (and gh) commands:

`gitsome`

- Setup GitHub integration with the current account:

`gh configure`

- List notifications for the current account (as would be seen in <https://github.com/notifications>):

`gh notifications`

- List the current account's starred repos, filtered by a given search string:

`gh starred "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python 3</span>`"`

- View the recent activity feed of a given GitHub repository:

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-pages/tldr</span>

- View the recent activity feed for a given GitHub user, using the default pager (e.g. `less`):

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torvalds</span>` -p`
