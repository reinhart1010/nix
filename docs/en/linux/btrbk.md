---
layout: page
title: linux/btrbk (English)
description: "A tool for creating snapshots and remote backups of btrfs subvolumes."
content_hash: b5329217c890a07a5e147858f6ddf150497aa0d7
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrbk

A tool for creating snapshots and remote backups of btrfs subvolumes.
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
