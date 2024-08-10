---
layout: page
title: common/git-config (English)
description: "Manage custom configuration options for Git repositories."
content_hash: ceba6062b2a23bbcd8051c1f9f1f2248081627f9
last_modified_at: 2024-08-10
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git config

Manage custom configuration options for Git repositories.
These configurations can be local (for the current repository) or global (for the current user).
More information: <https://git-scm.com/docs/git-config>.

- Globally set your name or email (this information is required to commit to a repository and will be included in all commits):

`git config --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.name|user.email</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Your Name|email@example.com</span>`"`

- List local or global configuration entries:

`git config --list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global</span>

- List only system configuration entries (stored in `/etc/gitconfig`), and show their file location:

`git config --list --system --show-origin`

- Get the value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Revert a global configuration entry to its default value:

`git config --global --unset alias.unstage`

- Edit the local Git configuration (`.git/config`) in the default editor:

`git config --edit`

- Edit the global Git configuration (`~/.gitconfig` by default or `$XDG_CONFIG_HOME/git/config` if such a file exists) in the default editor:

`git config --global --edit`
