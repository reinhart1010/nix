---
layout: page
title: common/git-imerge (English)
description: "Perform a merge or rebase between two Git branches incrementally."
content_hash: 38d0424f3bc86699f60237a7d579775680655883
related_topics:
  - title: español version
    url: /es/common/git-imerge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-imerge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-imerge.html
    icon: bi bi-globe
---
# git-imerge

Perform a merge or rebase between two Git branches incrementally.
Conflicts between branches are tracked down to pairs of individual commits, to simplify conflict resolution.
More information: <https://github.com/mhagger/git-imerge>.

- Start imerge-based rebase (checkout the branch to be rebased, first):

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_to_rebase_onto</span>

- Start imerge-based merge (checkout the branch to merge into, first):

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_to_be_merged</span>

- Show ASCII diagram of in-progress merge or rebase:

`git imerge diagram`

- Continue imerge operation after resolving conflicts (`git add` the conflicted files, first):

`git imerge continue --no-edit`

- Wrap up imerge operation, after all conflicts are resolved:

`git imerge finish`

- Abort imerge operation, and return to the previous branch:

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">previous_branch</span>
