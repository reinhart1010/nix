---
layout: page
title: linux/physlock (English)
description: "Lock all consoles and virtual terminals."
content_hash: dc916953074e27f7ab5286ae870591de03442b12
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# physlock

Lock all consoles and virtual terminals.
More information: <http://github.com/muennich/physlock>.

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
