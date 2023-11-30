---
layout: page
title: linux/playerctl (English)
description: "Control media players via MPRIS."
content_hash: 166586556fd09935dd651288f0e8dba4ce30ac86
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# playerctl

Control media players via MPRIS.
More information: <https://github.com/altdesktop/playerctl>.

- Toggle play:

`playerctl play-pause`

- Skip to the next track:

`playerctl next`

- Go back to the previous track:

`playerctl previous`

- List all players:

`playerctl --list-all`

- Send a command to a specific player:

`playerctl --player `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">player_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play-pause|next|previous|...</span>

- Send a command to all players:

`playerctl --all-players `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play-pause|next|previous|...</span>

- Display metadata about the current track:

`playerctl metadata --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Now playing: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}</span>`"`
