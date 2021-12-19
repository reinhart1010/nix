---
layout: page
title: common/gh-issue (English)
description: "Manage GitHub issues from the command-line."
content_hash: a641adbd87d6717ba374e46cde66c5904a05b956
---
# gh issue

Manage GitHub issues from the command-line.
More information: <https://cli.github.com/manual/gh_issue>.

- Print out the issue:

`gh issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Create a new issue in the web browser:

`gh issue create --web`

- List the last 10 issues with the `bug` label:

`gh issue list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- List closed issues made by a specific user:

`gh issue list --state closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display the status of issues relevant to the user, in a specific repository:

`gh issue status --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Reopen an issue:

`gh issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>
