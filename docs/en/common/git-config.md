---
layout: page
title: common/git-config (English)
description: "Manage custom configuration options for Git repositories."
content_hash: 13fb8b1d3cbfa8a161706fb91e53312ca77995f5
last_modified_at: 2023-11-12
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

- List only local configuration entries (stored in `.git/config` in the current repository):

`git config --list --local`

- List only global configuration entries (stored in `~/.gitconfig` by default or in `$XDG_CONFIG_HOME/git/config` if such a file exists):

`git config --list --global`

- List only system configuration entries (stored in `/etc/gitconfig`), and show their file location:

`git config --list --system --show-origin`

- Get the value of a given configuration entry:

`git config alias.unstage`

- Set the global value of a given configuration entry:

`git config --global alias.unstage "reset HEAD --"`

- Revert a global configuration entry to its default value:

`git config --global --unset alias.unstage`

- Edit the Git configuration for the current repository in the default editor:

`git config --edit`

- Edit the global Git configuration in the default editor:

`git config --global --edit`
