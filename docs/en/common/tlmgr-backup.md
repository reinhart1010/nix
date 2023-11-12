---
layout: page
title: common/tlmgr-backup (English)
description: "Manage backups of TeX Live packages."
content_hash: a1cf6ebbb4bf51d8ef255efa571768b74ae9c45e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr backup

Manage backups of TeX Live packages.
The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Make a backup of one or more packages:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Make a backup of all packages:

`tlmgr backup --all`

- Make a backup to a custom directory:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_directory</span>

- Remove a backup of one or more packages:

`tlmgr backup clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove all backups:

`tlmgr backup clean --all`
