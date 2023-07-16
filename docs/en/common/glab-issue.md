---
layout: page
title: common/glab-issue (English)
description: "Manage GitLab issues."
content_hash: f077bdcebe3605dff21806160f27b06bce3ce0db
last_modified_at: 2023-07-16
---
# glab issue

Manage GitLab issues.
More information: <https://glab.readthedocs.io/en/latest/issue>.

- Display a specific issue:

`glab issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Display a specific issue in the default web browser:

`glab issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>` --web`

- Create a new issue in the default web browser:

`glab issue create --web`

- List the last 10 issues with the `bug` label:

`glab issue list --per-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- List closed issues made by a specific user:

`glab issue list --closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Reopen a specific issue:

`glab issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>
