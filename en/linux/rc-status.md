---
layout: page
title: linux/rc-status (English)
description: "Show status info about runlevels."
content_hash: 5e62c08706b28beebf63648af938a3274bcecc14
---
# rc-status

Show status info about runlevels.
See also `openrc`.

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
