---
layout: page
title: common/gh-pr (English)
description: "Manage GitHub pull requests from the command-line."
content_hash: 8db1ece90d21baee102155801537fb1641779abd
---
# gh pr

Manage GitHub pull requests from the command-line.
More information: <https://cli.github.com/manual/gh_pr>.

- Create a pull request:

`gh pr create`

- Check out a specific pull request locally:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- View the changes made in the pull request for the current branch:

`gh pr diff`

- Approve the pull request for the current branch:

`gh pr review --approve`

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Edit a pull request interactively:

`gh pr edit`

- Edit the base branch of a pull request:

`gh pr edit --base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Check the status of the current repository's pull requests:

`gh pr status`
