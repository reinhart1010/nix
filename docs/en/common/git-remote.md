---
layout: page
title: common/git-remote (English)
description: "Manage set of tracked repositories (\"remotes\")."
content_hash: 574adb370c52085f707b668a2e407be41c44a915
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/git-remote.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-remote.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-remote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git remote

Manage set of tracked repositories ("remotes").
More information: <https://git-scm.com/docs/git-remote>.

- List existing remotes with their names and URLs:

`git remote -v`

- Show information about a remote:

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Add a remote:

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_url</span>

- Change the URL of a remote (use `--add` to keep the existing URL):

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_url</span>

- Show the URL of a remote:

`git remote get-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Remove a remote:

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Rename a remote:

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>
