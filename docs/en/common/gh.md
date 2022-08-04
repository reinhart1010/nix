---
layout: page
title: common/gh (English)
description: "Work seamlessly with GitHub from the command-line."
content_hash: 22bd932821e492e3bd0d07800b8cc6e4211ae9a1
related_topics:
  - title: Indonesia version
    url: /id/common/gh.html
    icon: bi bi-globe
---
# gh

Work seamlessly with GitHub from the command-line.
Some subcommands such as `gh config` have their own usage documentation.
More information: <https://cli.github.com/>.

- Clone a GitHub repository locally:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Create a new issue:

`gh issue create`

- View and filter the open issues of the current repository:

`gh issue list`

- View an issue in the default web browser:

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Create a pull request:

`gh pr create`

- View a pull request in the default web browser:

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check out a specific pull request locally:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check the status of a repository's pull requests:

`gh pr status`
