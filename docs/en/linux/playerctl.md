---
layout: page
title: linux/playerctl (English)
description: "Utility to control different media players."
content_hash: 3037d54b3938a588e1e31199ed685990e433bcdd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# playerctl

Utility to control different media players.
More information: <https://github.com/altdesktop/playerctl>.

- Toggle play:

`playerctl play-pause`

- Next media:

`playerctl next`

- Previous media:

`playerctl previous`

- List all players:

`playerctl --list-all`

- Send a command to a specific player:

`playerctl --player=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">player_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Send a command to all players:

`playerctl --all-players `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Show now playing:

`playerctl metadata --format "Now playing: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artist</span>` - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">album</span>` - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`"`
