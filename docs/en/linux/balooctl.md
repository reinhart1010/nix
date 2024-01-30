---
layout: page
title: linux/balooctl (English)
description: "File indexing and searching framework for KDE Plasma."
content_hash: eb68ecd240d2ef47dd6a6e47cc0d7d9b05a55358
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/linux/balooctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# balooctl

File indexing and searching framework for KDE Plasma.
More information: <https://wiki.archlinux.org/index.php/Baloo>.

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

- Display help:

`balooctl --help`
