---
layout: page
title: common/gt (English)
description: "Create and manage sequences of dependent code changes (stacks) for Git and GitHub."
content_hash: 0e3ebc7cc2f7d36a5fd24f0a70e5b4f9975bf7e5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gt

Create and manage sequences of dependent code changes (stacks) for Git and GitHub.
More information: <https://docs.graphite.dev>.

- Authenticate the CLI with Graphite's API:

`gt auth --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">graphite_cli_auth_token</span>

- Initialise `gt` for the repository in the current directory:

`gt repo init`

- Create a new branch stacked on top of the current branch and commit staged changes:

`gt branch create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new commit and fix upstack branches:

`gt commit create -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>

- Force push all branches in the current stack to GitHub and create or update PRs:

`gt stack submit`

- Log all tracked stacks:

`gt log short`

- Print help for a specified subcommand:

`gt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
