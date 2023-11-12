---
layout: page
title: common/git-reauthor (English)
description: "Change details about an author identity. Since this command rewrites the Git history, `--force` will be needed when pushing next time."
content_hash: b77ac3e96b97b58b83abfe6d6d03398ca2207753
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git reauthor

Change details about an author identity. Since this command rewrites the Git history, `--force` will be needed when pushing next time.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- Change an author's email and name across the whole Git repository:

`git reauthor --old-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old@example.com</span>` --correct-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new@example.com</span>` --correct-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Change the email and name to the ones defined in the Git config:

`git reauthor --old-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old@example.com</span>` --use-config`

- Change the email and name of all commits, regardless of their original author:

`git reauthor --all --correct-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name@example.com</span>` --correct-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
