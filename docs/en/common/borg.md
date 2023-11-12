---
layout: page
title: common/borg (English)
description: "Deduplicating backup tool."
content_hash: ff40c8cd6e4ab70919928dad341d075ad09ed465
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/borg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/borg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/borg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/borg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# borg

Deduplicating backup tool.
Creates local or remote backups that are mountable as filesystems.
More information: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialize a (local) repository:

`borg init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>

- Backup a directory into the repository, creating an archive called "Monday":

`borg create --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>

- List all archives in a repository:

`borg list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>

- Extract a specific directory from the "Monday" archive in a remote repository, excluding all `*.ext` files:

`borg extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Prune a repository by deleting all archives older than 7 days, listing changes:

`borg prune --keep-within `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>

- Mount a repository as a FUSE filesystem:

`borg mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mountpoint</span>

- Display help on creating archives:

`borg create --help`
