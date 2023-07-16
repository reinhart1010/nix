---
layout: page
title: common/glab (English)
description: "Work seamlessly with GitLab."
content_hash: ff0b6978a9f9c13e9197902545ae991d467c4267
last_modified_at: 2023-07-16
---
# glab

Work seamlessly with GitLab.
Some subcommands such as `glab config` have their own usage documentation.
More information: <https://github.com/profclems/glab>.

- Clone a GitLab repository locally:

`glab repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Create a new issue:

`glab issue create`

- View and filter the open issues of the current repository:

`glab issue list`

- View an issue in the default browser:

`glab issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Create a merge request:

`glab mr create`

- View a pull request in the default web browser:

`glab mr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Check out a specific pull request locally:

`glab mr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>
