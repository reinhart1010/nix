---
layout: page
title: linux/btrbk (English)
description: "Create snapshots and remote backups of btrfs subvolumes."
content_hash: a2af3f8c144cfcd64f42e2eb93dc126642aace8c
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# btrbk

Create snapshots and remote backups of btrfs subvolumes.
More information: <https://digint.ch/btrbk/doc/readme.html>.

- Print statistics about configured subvolumes and snapshots:

`sudo btrbk stats`

- List configured subvolumes and snapshots:

`sudo btrbk list`

- Print what would happen in a run without making the displayed changes:

`sudo btrbk --verbose dryrun`

- Run backup routines verbosely, show progress bar:

`sudo btrbk --progress --verbose run`

- Only create snapshots for configured subvolumes:

`sudo btrbk snapshot`
