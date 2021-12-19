---
layout: page
title: common/gh-pr-create (English)
description: "Manage GitHub pull requests from the command-line."
content_hash: 0a8f578b6b1950f770c59169a883f93b1b222de4
---
# gh pr create

Manage GitHub pull requests from the command-line.
More information: <https://cli.github.com/manual/gh_pr_create>.

- Interactively create a pull request:

`gh pr create`

- Create a pull request, determining the title and description from the commit messages of the current branch:

`gh pr create --fill`

- Create a draft pull request:

`gh pr create --draft`

- Create a pull request specifying the base branch, title, and description:

`gh pr create --base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_branch</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body</span>`"`

- Start opening a pull request in the browser:

`gh pr create --web`
