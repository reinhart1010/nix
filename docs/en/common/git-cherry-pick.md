---
layout: page
title: common/git-cherry-pick (English)
description: "Apply the changes introduced by existing commits to the current branch."
content_hash: 1d2b06e32d0a3a662c4a1469e4d5ae96219c6416
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry-pick

Apply the changes introduced by existing commits to the current branch.
To apply changes to another branch, first use `git checkout` to switch to the desired branch.
More information: <https://git-scm.com/docs/git-cherry-pick>.

- Apply a commit to the current branch:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Apply a range of commits to the current branch (see also `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_commit</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_commit</span>

- Apply multiple (non-sequential) commits to the current branch:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Add the changes of a commit to the working directory, without creating a commit:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
