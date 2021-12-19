---
layout: page
title: common/git-revert (English)
description: "Create new commits which reverse the effect of earlier ones."
content_hash: 261613e626400024f0cd160b7bb6880919acdc5e
related_topics:
  - title: español version
    url: /es/common/git-revert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-revert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-revert.html
    icon: bi bi-globe
---
# git revert

Create new commits which reverse the effect of earlier ones.
More information: <https://git-scm.com/docs/git-revert>.

- Revert the most recent commit:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Revert the 5th last commit:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Revert multiple commits:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name~5..branch_name~2</span>

- Don't create new commits, just change the working tree:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
