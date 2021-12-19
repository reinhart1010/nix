---
layout: page
title: linux/ytfzf (English)
description: "A POSIX script that helps you find and download videos and music."
content_hash: 216b13b35428ab20efdcf9cb5609b5ecdf9c39b0
---
# ytfzf

A POSIX script that helps you find and download videos and music.
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
