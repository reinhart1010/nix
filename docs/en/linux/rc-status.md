---
layout: page
title: linux/rc-status (English)
description: "Show status info about runlevels."
content_hash: 12fd1f5607c64f1ddbd1d23fefad82b445fc7871
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rc-status

Show status info about runlevels.
See also `openrc`.
More information: <https://manned.org/rc-status>.

- Show a summary of services and their status:

`rc-status`

- Include services in all runlevels in the summary:

`rc-status --all`

- List services that have crashed:

`rc-status --crashed`

- List manually started services:

`rc-status --manual`

- List supervised services:

`rc-status --supervised`

- Get the current runlevel:

`rc-status --runlevel`

- List all runlevels:

`rc-status --list`
