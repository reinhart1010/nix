---
layout: page
title: common/yt-dlp (English)
description: "A youtube-dl fork with additional features and fixes."
content_hash: 8fc53a22369930d68b11bf04f5bc12d26f783de9
last_modified_at: 2024-11-15
related_topics:
  - title: 한국어 version
    url: /ko/common/yt-dlp.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/yt-dlp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yt-dlp

A youtube-dl fork with additional features and fixes.
Download videos from YouTube and other websites.
See also: `yt-dlp`, `ytfzf`.
More information: <https://github.com/yt-dlp/yt-dlp>.

- Download a video or playlist (with the default options from command below):

`yt-dlp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- List the available downloadable formats for a video:

`yt-dlp --list-formats "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Download a video or playlist using the best MP4 video available (default is "bv\*+ba/b"):

`yt-dlp --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Extract audio from a video (requires ffmpeg or ffprobe):

`yt-dlp --extract-audio "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Specify audio format and audio quality of extracted audio (between 0 (best) and 10 (worst), default = 5):

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` --audio-quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Download only the second, fourth, fifth, sixth, and last items in a playlist (the first item is 1, not 0):

`yt-dlp --playlist-items 2,4:6,-1 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA</span>`"`

- Download all playlists of a YouTube channel/user keeping each playlist in a separate directory:

`yt-dlp -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/user/TheLinuxFoundation/playlists</span>`"`

- Download a Udemy course keeping each chapter in a separate directory:

`yt-dlp -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.udemy.com/java-tutorial</span>`"`
