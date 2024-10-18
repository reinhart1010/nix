---
layout: page
title: linux/lbu (English)
description: "Manage `apk` overlay files on a diskless Alpine Linux system."
content_hash: 0f66ff5d8ac618853a338d4c34fecbd3792980f5
last_modified_at: 2024-10-18
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/lbu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lbu

Manage `apk` overlay files on a diskless Alpine Linux system.
Note: subcommands like `include` write to `/etc`, which is stored in RAM. You need to run `lbu commit` to save the changes.
More information: <https://wiki.alpinelinux.org/wiki/Alpine_local_backup>.

- Commit changes to persistent storage (only files in `/etc` by default):

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ci|commit</span>

- List files that would be saved using `commit`:

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">st|status</span>

- Display changes in tracked files that would be saved using `commit`:

`lbu diff`

- Include a specific file or directory in the `apk` overlay:

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|inc|include</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Exclude a specific file or directory in `/etc` from the `apk` overlay:

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ex|exclude|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Display the list of manually included/excluded files:

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc|include|ex|exclude</span>` -l`

- List backups (previously created overlays):

`lbu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lb|list-backup</span>

- Revert to a backup overlay:

`lbu revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">overlay_filename.tar.gz</span>
