---
layout: page
title: linux/balooctl (English)
description: "File indexing and searching framework for KDE Plasma."
content_hash: 6d212c9b3eeaf7702eb8e40db0775f19b96227e3
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/balooctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# balooctl

File indexing and searching framework for KDE Plasma.
More information: <https://wiki.archlinux.org/index.php/Baloo>.

- Display help:

`balooctl`

- Display the status of the indexer:

`balooctl status`

- Enable/Disable the file indexer:

`balooctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- Clean the index database:

`balooctl purge`

- Suspend the file indexer:

`balooctl suspend`

- Resume the file indexer:

`balooctl resume`

- Display the disk space used by Baloo:

`balooctl indexSize`

- Check for any unindexed files and index them:

`balooctl check`
