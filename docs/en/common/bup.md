---
layout: page
title: common/bup (English)
description: "Backup system based on the Git packfile format, providing incremental saves and global deduplication."
content_hash: 6f2511e810dd1609b0859fde7258610b47cd950d
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/bup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bup

Backup system based on the Git packfile format, providing incremental saves and global deduplication.
More information: <https://github.com/bup/bup>.

- Initialize a backup repository in the specified local directory:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` init`

- Prepare a given directory before taking a backup:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Backup a directory to the repository:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show the backup snapshots currently stored in the repository:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` ls`

- Restore a specific backup snapshot to a target directory:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>
