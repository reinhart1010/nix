---
layout: page
title: linux/extundelete (English)
description: "Recover deleted files from ext3 or ext4 partitions by parsing the journal."
content_hash: 18d381ff4360691d9ad645252840655bb801ba61
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# extundelete

Recover deleted files from ext3 or ext4 partitions by parsing the journal.
See also `date` for Unix time information and `umount` for unmounting partitions.
More information: <https://extundelete.sourceforge.net>.

- Restore all deleted files inside partition N on device X:

`sudo extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-all`

- Restore a file from a path relative to root (Do not start the path with `/`):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Restore a directory from a path relative to root (Do not start the path with `/`):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Restore all files deleted after January 1st, 2020 (in Unix time):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-all --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1577840400</span>
