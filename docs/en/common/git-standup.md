---
layout: page
title: common/git-standup (English)
description: "See commits from a specified user."
content_hash: 4d2fcc74ad84001c609442ee6168a4da491e7f3e
last_modified_at: 2024-10-07
tldri18n_status: 2
---
# git standup

See commits from a specified user.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>.

- Show a given author's commits from the last 10 days:

`git standup -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|email</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Show a given author's commits from the last 10 days and whether they are GPG signed:

`git standup -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|email</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -g`

- Show all the commits from all contributors for the last 10 days:

`git standup -a all -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Display help:

`git standup -h`
