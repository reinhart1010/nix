---
layout: page
title: osx/tmutil (English)
description: "Utility for managing Time Machine backups. Most verbs require root privileges."
content_hash: 18a0807ca9cb7005c26bf7c833b17adc96a0d89a
related_topics:
  - title: Deutsch version
    url: /de/osx/tmutil.html
    icon: bi bi-globe
---
# tmutil

Utility for managing Time Machine backups. Most verbs require root privileges.
More information: <https://ss64.com/osx/tmutil.html>.

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
