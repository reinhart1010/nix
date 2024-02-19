---
layout: page
title: common/bup (English)
description: "Backup system based on the Git packfile format, providing incremental saves and global deduplication."
content_hash: c70afd88d733aabd566e8a5b1177607413526427
last_modified_at: 2024-02-19
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

- Initialize a backup repository in a given local [d]irectory:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` init`

- Prepare a given [d]irectory before taking a backup:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Backup a [d]irectory to the repository specifying its [n]ame:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show the backup snapshots currently stored in the repository:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` ls`

- Restore a specific backup snapshot to a target dire[C]tory:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_name</span>
