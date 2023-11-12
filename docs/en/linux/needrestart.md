---
layout: page
title: linux/needrestart (English)
description: "Check which daemons need to be restarted after library upgrades."
content_hash: 94ce2ad22483adb863d73f40c75f67d55db063c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# needrestart

Check which daemons need to be restarted after library upgrades.
More information: <https://github.com/liske/needrestart>.

- List outdated processes:

`needrestart`

- Interactively restart services:

`sudo needrestart`

- List outdated processes in [v]erbose or [q]uiet mode:

`needrestart -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v|q</span>

- Check if the [k]ernel is outdated:

`needrestart -k`

- Check if the CPU microcode is outdated:

`needrestart -w`

- List outdated processes in [b]atch mode:

`needrestart -b`

- List outdated processed using a specific [c]onfiguration file:

`needrestart -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Display help:

`needrestart --help`
