---
layout: page
title: common/tlmgr-backup (English)
description: "Manage backups of TeX Live packages."
content_hash: 07ef700b0a06adb890285c5565b2f0ecacea4ac3
---
# tlmgr backup

Manage backups of TeX Live packages.
The default backup location is saved in the `backupdir` setting, which can be optained with `tlmgr option`.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Make a backup of one or more packages:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Make a backup of all packages:

`tlmgr backup --all`

- Make a backup to a specific directory:

`tlmgr backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_directory</span>

- Remove a backup of one or more packages:

`tlmgr backup clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove all backups:

`tlmgr backup clean --all`
