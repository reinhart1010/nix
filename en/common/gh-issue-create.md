---
layout: page
title: common/gh-issue-create (English)
description: "Create GitHub issues on a repository from the command-line."
content_hash: 4174e69e44026580fa083aaa880a50a1329547c5
---
# gh issue create

Create GitHub issues on a repository from the command-line.
More information: <https://cli.github.com/manual/gh_issue_create>.

- Create a new issue against the current repository interactively:

`gh issue create`

- Create a new issue with the `bug` label interactively:

`gh issue create --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- Create a new issue interactively and assign it to the specified users:

`gh issue create --assignee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2,...</span>

- Create a new issue with a title, body and assign it to the current user:

`gh issue create --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body</span>`" --assignee "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@me</span>`"`

- Create a new issue interactively, reading the body text from a file:

`gh issue create --body-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a new issue in the default web browser:

`gh issue create --web`

- Display the help:

`gh issue create --help`
