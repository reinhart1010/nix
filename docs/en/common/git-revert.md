---
layout: page
title: common/git-revert (English)
description: "Create new commits which reverse the effect of earlier ones."
content_hash: d7f07c3140c0175d989630ec30b90c4e975b91af
last_modified_at: 2025-03-02
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
  - title: 한국어 version
    url: /ko/common/git-revert.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-revert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git revert

Create new commits which reverse the effect of earlier ones.
More information: <https://git-scm.com/docs/git-revert>.

- Revert the most recent commit:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Revert the 5th last commit:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Revert a specific commit:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9</span>

- Revert multiple commits:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name~5..branch_name~2</span>

- Don't create new commits, just change the working tree:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--no-commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>

- Cancel a Git revert after a merge conflict:

`git revert --abort`
