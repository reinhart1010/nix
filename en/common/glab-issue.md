---
layout: page
title: common/glab-issue (English)
description: "Manage GitLab issues from the command-line."
content_hash: 95ad3d97cab795d804236de0152144a804eaebf5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab issue

Manage GitLab issues from the command-line.
More information: <https://glab.readthedocs.io/en/latest/issue>.

- Display a specific issue:

`glab issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Create a new issue in the default web browser:

`glab issue create --web`

- List the last 10 issues with the `bug` label:

`glab issue list --per-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- List closed issues made by a specific user:

`glab issue list --closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Reopen a specific issue:

`glab issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>
