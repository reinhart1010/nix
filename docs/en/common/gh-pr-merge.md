---
layout: page
title: common/gh-pr-merge (English)
description: "Merge GitHub pull requests."
content_hash: 433d3f3133a414eceee397ff66beaec26284c902
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gh pr merge

Merge GitHub pull requests.
More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Merge the specified pull request, interactively:

`gh pr merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Merge the pull request, removing the branch on both the local and the remote:

`gh pr merge --delete-branch`

- Merge the current pull request with the specified merge strategy:

`gh pr merge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">merge|squash|rebase</span>

- Merge the current pull request with the specified merge strategy and commit message:

`gh pr merge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">merge|squash|rebase</span>` --subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>

- Squash the current pull request into one commit with the message body and merge:

`gh pr merge --squash --body="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message_body</span>`"`

- Display help:

`gh pr merge --help`
