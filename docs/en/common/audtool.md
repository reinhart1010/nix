---
layout: page
title: common/audtool (English)
description: "Control Audacious using commands."
content_hash: e71b6a0b79ea1dc46fd3616751cfa172edc6bbd9
last_modified_at: 2024-06-05
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/audtool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># audtool

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
