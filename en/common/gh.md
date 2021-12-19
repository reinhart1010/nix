---
layout: page
title: common/gh (English)
description: "Work seamlessly with GitHub from the command-line."
content_hash: 622950e14540abde21786dfe38a1b20028413102
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

- View an issue in the browser:

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Create a pull request:

`gh pr create`

- View a pull request in the browser:

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Locally check out the branch of a pull request, given its number:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check the status of a repository's pull requests:

`gh pr status`
