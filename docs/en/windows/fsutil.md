---
layout: page
title: windows/fsutil (English)
description: "Displays information about file system volumes."
content_hash: c8b1fea4e64824952f130d7db89bb3bb47206b15
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fsutil

Displays information about file system volumes.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- Display a list of volumes:

`fsutil volume list`

- Display information about a volume's file system:

`fsutil fsInfo volumeInfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter|volume_path</span>

- Display the current state of the file system auto-repair for all volumes:

`fsutil repair state`

- Display the dirty bit state of all volumes:

`fsutil dirty query`

- Set the dirty bit state of a volume:

`fsutil dirty set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter|volume_path</span>
