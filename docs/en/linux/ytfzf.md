---
layout: page
title: linux/ytfzf (English)
description: "Find and download videos and music. Written in POSIX shell."
content_hash: d9bc1e02ac878cff9ceb7ec55d8043c9ce599fb8
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# ytfzf

Find and download videos and music. Written in POSIX shell.
See also: `youtube-dl`, `yt-dlp`, `instaloader`.
More information: <https://github.com/pystardust/ytfzf>.

- Search for videos on YouTube with thumbnail previews:

`ytfzf --show-thumbnails `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Play only the audio of the first item in a loop:

`ytfzf --audio-only --auto-select --loop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Download a video from the history:

`ytfzf --download --choose-from-history`

- Play all the music found in a search:

`ytfzf --audio-only --select-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- See the trending videos in an external menu:

`ytfzf --trending --ext-menu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Search on PeerTube instead of YouTube:

`ytfzf --peertube `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>
