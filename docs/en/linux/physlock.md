---
layout: page
title: linux/physlock (English)
description: "Lock all consoles and virtual terminals."
content_hash: 49b11238f93fd919da5d030b699471476a6121f4
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# physlock

Lock all consoles and virtual terminals.
More information: <https://github.com/muennich/physlock>.

- Lock every console (require current user or root to unlock):

`physlock`

- Mute kernel messages on console while locked:

`physlock -m`

- Disable SysRq mechanism while locked:

`physlock -s`

- Display a message before the password prompt:

`physlock -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Locked!</span>`"`

- Fork and detach physlock (useful for suspend or hibernate scripts):

`physlock -d`
