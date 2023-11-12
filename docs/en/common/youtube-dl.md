---
layout: page
title: common/youtube-dl (English)
description: "Download videos from YouTube and other websites."
content_hash: a0f7e52362fe37e9364f32339360e74166d8c017
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/youtube-dl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/youtube-dl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/youtube-dl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/youtube-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# youtube-dl

Download videos from YouTube and other websites.
More information: <http://rg3.github.io/youtube-dl/>.

- Download a video or playlist:

`youtube-dl '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- List all formats that a video or playlist is available in:

`youtube-dl --list-formats '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Download a video or playlist at a specific quality:

`youtube-dl --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best[height<=480]</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Download the audio from a video and convert it to an MP3:

`youtube-dl -x --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Download the best quality audio and video and merge them:

`youtube-dl -f bestvideo+bestaudio '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Download video(s) as MP4 files with custom filenames:

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Download a particular language's subtitles along with the video:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Download a playlist and extract MP3s from it:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_to_playlist</span>
