---
layout: page
title: common/dolt-commit (English)
description: "Commit staged changes to tables."
content_hash: 4300250786f1f78a0ccaebbac707a6d9e7c7943a
---
# dolt commit

Commit staged changes to tables.
More information: <https://docs.dolthub.com/interfaces/cli#dolt-commit>.

- Commit all staged changes, opening the editor specified by `$EDITOR` to enter the commit message:

`dolt commit`

- Commit all staged changes with the specified message:

`dolt commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>`"`

- Stage all unstaged changes to tables before committing:

`dolt commit --all`

- Use the specified ISO 8601 commit date (defaults to current date and time):

`dolt commit --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-12-31T00:00:00</span>`"`

- Use the specified author for the commit:

`dolt commit --author "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author_name</span>` <`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author_email</span>`>"`

- Allow creating an empty commit, with no changes:

`dolt commit --allow-empty`

- Ignore foreign key warnings:

`dolt commit --force`
