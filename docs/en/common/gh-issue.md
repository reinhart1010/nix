---
layout: page
title: common/gh-issue (English)
description: "Manage GitHub issues."
content_hash: 600b0734010558d483d32db6fab09a5816608e13
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gh issue

Manage GitHub issues.
More information: <https://cli.github.com/manual/gh_issue>.

- Display a specific issue:

`gh issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Display a specific issue in the default web browser:

`gh issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>` --web`

- Create a new issue in the default web browser:

`gh issue create --web`

- List the last 10 issues with the `bug` label:

`gh issue list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- List closed issues made by a specific user:

`gh issue list --state closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display the status of issues relevant to the user, in a specific repository:

`gh issue status --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Reopen a specific issue:

`gh issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>
