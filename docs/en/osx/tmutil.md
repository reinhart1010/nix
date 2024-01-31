---
layout: page
title: osx/tmutil (English)
description: "Utility for managing Time Machine backups. Most verbs require root privileges."
content_hash: 1b684ee3eace9223def27d781bddca57d8593358
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/tmutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/tmutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmutil

Utility for managing Time Machine backups. Most verbs require root privileges.
More information: <https://keith.github.io/xcode-man-pages/tmutil.8.html>.

- Set an HFS+ drive as the backup destination:

`sudo tmutil setdestination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/disk_mount_point</span>

- Set an APF share or SMB share as the backup destination:

`sudo tmutil setdestination "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol://user[:password]@host/share</span>`"`

- Append the given destination to the list of destinations:

`sudo tmutil setdestination -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Enable automatic backups:

`sudo tmutil enable`

- Disable automatic backups:

`sudo tmutil disable`

- Start a backup, if one is not running already, and release control of the shell:

`sudo tmutil startbackup`

- Start a backup and block until the backup is finished:

`sudo tmutil startbackup -b`

- Stop a backup:

`sudo tmutil stopbackup`
