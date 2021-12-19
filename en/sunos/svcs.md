---
layout: page
title: sunos/svcs (English)
description: "List information about running services."
content_hash: ebabb92f0d57783324d15ecbd0ecf4b9e47017d9
---
# svcs

List information about running services.
More information: <https://www.unix.com/man-page/linux/1/svcs>.

- List all running services:

`svcs`

- List services that are not running:

`svcs -vx`

- List information about a service:

`svcs apache`

- Show location of service log file:

`svcs -L apache`

- Display end of a service log file:

`tail $(svcs -L apache)`
