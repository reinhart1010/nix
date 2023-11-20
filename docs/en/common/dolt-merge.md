---
layout: page
title: common/dolt-merge (English)
description: "Join two or more development histories together."
content_hash: d138308775ffe8b3259ce176a40cdfa88577526d
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt merge

Join two or more development histories together.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- Incorporate changes from the named commits into the current branch:

`dolt merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Incorporate changes from the named commits into the current branch without updating the commit history:

`dolt merge --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Merge a branch and create a merge commit even when the merge resolves as a fast-forward:

`dolt merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Merge a branch and create a merge commit with a specific commit message:

`dolt merge --no-ff -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Abort the current conflict resolution process:

`dolt merge --abort`
