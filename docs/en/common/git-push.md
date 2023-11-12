---
layout: page
title: common/git-push (English)
description: "Push commits to a remote repository."
content_hash: 2a6b5ce100b854c37f4c6a7a09190a511d4834c6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git push

Push commits to a remote repository.
More information: <https://git-scm.com/docs/git-push>.

- Send local changes in the current branch to its default remote counterpart:

`git push`

- Send changes from a specific local branch to its remote counterpart:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_branch</span>

- Send changes from a specific local branch to its remote counterpart, and set the remote one as the default push/pull target of the local one:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_branch</span>

- Send changes from a specific local branch to a specific remote branch:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_branch</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_branch</span>

- Send changes on all local branches to their counterparts in a given remote repository:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Delete a branch in a remote repository:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_branch</span>

- Remove remote branches that don't have a local counterpart:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Publish tags that aren't yet in the remote repository:

`git push --tags`
