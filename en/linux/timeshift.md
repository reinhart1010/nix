---
layout: page
title: linux/timeshift (English)
description: "System restore utility."
content_hash: c63baa272dca0af332d0ff9e509e9c67db2f3b1d
---
# timeshift

System restore utility.
More information: <https://github.com/teejee2008/timeshift>.

- List snapshots:

`sudo timeshift --list`

- Create a new snapshot (if scheduled):

`sudo timeshift --check`

- Create a new snapshot (even if not scheduled):

`sudo timeshift --create`

- Restore a snapshot (selecting which snapshot to restore interactively):

`sudo timeshift --restore`

- Restore a specific snapshot:

`sudo timeshift --restore --snapshot '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot</span>`'`

- Delete a specific snapshot:

`sudo timeshift --delete --snapshot '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot</span>`'`
