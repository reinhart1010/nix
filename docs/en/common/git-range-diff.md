---
layout: page
title: common/git-range-diff (English)
description: "Compare two commit ranges (e.g. two versions of a branch)."
content_hash: bf5fb7902f3b6dc844c08867805979e683c01cbd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git range-diff

Compare two commit ranges (e.g. two versions of a branch).
More information: <https://git-scm.com/docs/git-range-diff>.

- Diff the changes of two individual commits:

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>`^! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>`^!`

- Diff the changes of ours and theirs from their common ancestor, e.g. after an interactive rebase:

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theirs</span>`...`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ours</span>

- Diff the changes of two commit ranges, e.g. to check whether conflicts have been resolved appropriately when rebasing commits from `base1` to `base2`:

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rev1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base2</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rev2</span>
