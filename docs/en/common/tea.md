---
layout: page
title: common/tea (English)
description: "A command-line tool to interact with Gitea servers."
content_hash: 6dbe8ba8898b373a1bdd35e67d7d8acfb60fb2b3
---
# tea

A command-line tool to interact with Gitea servers.
More information: <https://gitea.com/gitea/tea>.

- Log into a Gitea server:

`tea login add --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" --token "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>`"`

- Display all repositories:

`tea repos ls`

- Display a list of issues:

`tea issues ls`

- Display a list of issues for a specific repository:

`tea issues ls --repo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>`"`

- Create a new issue:

`tea issues create --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body</span>`"`

- Display a list of open pull requests:

`tea pulls ls`

- Open the current repository in a browser:

`tea open`
