---
layout: page
title: common/audtool (English)
description: "Control Audacious using commands."
content_hash: e71b6a0b79ea1dc46fd3616751cfa172edc6bbd9
last_modified_at: 2024-06-06
related_topics:
  - title: español version
    url: /es/common/audtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audtool

Control Audacious using commands.
More information: <https://manned.org/audtool>.

- Play/pause audio playback:

`audtool playback-playpause`

- Print artist, album, and song name of currently playing song:

`audtool current-song`

- Set volume of audio playback:

`audtool set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Skip to the next song:

`audtool playlist-advance`

- Print the bitrate of the current song in kilobits:

`audtool current-song-bitrate-kbps`

- Open Audacious in full-screen if hidden:

`audtool mainwin-show`

- Display help:

`audtool help`

- Display settings:

`audtool preferences-show`
