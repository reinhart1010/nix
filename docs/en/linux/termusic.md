---
layout: page
title: linux/termusic (English)
description: "A terminal music player written in Rust that uses vim-like key bindings."
content_hash: 8871e2feb4afa44109adf1612154222b8f3242f3
last_modified_at: 2024-11-09
tldri18n_status: 2
---
# termusic

A terminal music player written in Rust that uses vim-like key bindings.
See also: `cmus`, `ncmpcpp`, `audacious`.
More information: <https://github.com/tramhao/termusic>.

- Open termusic to a specific directory. (It can be set permanently in `~/.config/termusic/config.toml`):

`termusic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Disable showing the album cover for a specific file:

`termusic -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/music_file</span>

- Display help:

`termusic --help`
