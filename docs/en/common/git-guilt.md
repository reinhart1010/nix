---
layout: page
title: common/git-guilt (English)
description: "Show total blame count for files with unstaged changes or calculate the change in blame between two revisions."
content_hash: 329e58ef8c71a41cb7cec2f5de1744e3c1daf954
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git guilt

Show total blame count for files with unstaged changes or calculate the change in blame between two revisions.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-guilt>.

- Show total blame count:

`git guilt`

- Calculate the change in blame between two revisions:

`git guilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last_revision</span>

- Show author emails instead of names:

`git guilt --email`

- Ignore whitespace only changes when attributing blame:

`git guilt --ignore-whitespace`

- Find blame delta over the last three weeks:

`git guilt 'git log --until="3 weeks ago" --format="%H" -n 1'`

- Find blame delta over the last three weeks (git 1.8.5+):

`git guilt @{3.weeks.ago}`
