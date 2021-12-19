---
layout: page
title: common/pueue-reset (English)
description: "Kill everything and reset."
content_hash: 81574eb1c5ad0c98d0f5b55cb4598628994a7aaa
---
# pueue reset

Kill everything and reset.
More information: <https://github.com/Nukesor/pueue>.

- Kill all tasks and remove everything (logs, status, groups, task IDs):

`pueue reset`

- Kill all tasks, terminate their children, and reset everything:

`pueue reset --children`

- Reset without asking for confirmation:

`pueue reset --force`
