---
layout: page
title: common/tlmgr-restore (English)
description: "Restore package backups created with `tlmgr backup`."
content_hash: cc0586d9ad850c70fec8ac4aa2c100cc257cfacf
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tlmgr restore

Restore package backups created with `tlmgr backup`.
The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all available backup revisions for all packages:

`tlmgr restore`

- List all available backup revisions for a specific package:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Restore a specific revision of a specific package:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Restore the latest revision of all backed-up packages:

`tlmgr restore --all`

- Restore a package from a custom backup directory:

`tlmgr restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>` --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_directory</span>

- Perform a dry-run and print all taken actions without making them:

`tlmgr restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>
