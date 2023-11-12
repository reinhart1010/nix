---
layout: page
title: common/dolt-merge (English)
description: "Join two or more development histories together."
content_hash: 320a82505b0b3296cc5639f596a34b0c8c85b45f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dolt merge

Join two or more development histories together.
More information: <https://github.com/dolthub/dolt>.

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
