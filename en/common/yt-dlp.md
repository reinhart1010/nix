---
layout: page
title: common/yt-dlp (English)
description: "A youtube-dl fork with additional features and fixes."
content_hash: 9f3d2a633ac28031ef2ccfd0590f8cce44362cf9
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yt-dlp

A youtube-dl fork with additional features and fixes.
Download videos from YouTube and other websites.
More information: <https://github.com/yt-dlp/yt-dlp>.

- Download a video or playlist (with the default options from command below):

`yt-dlp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Download a video with a defined format. In this case merging the best video format with the best audio format (Default):

`yt-dlp --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bv*+ba/b</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Extract audio from videos (required ffmpeg or ffprobe):

`yt-dlp --extract-audio "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Specify audio format of extracted audio (best(default), aac, flac, mp3, m4a, opus, vorbis, wav, alac):

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Specify audio quality of extracted audio (between 0 (best) and 10 (worst), default = 5):

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` --audio-quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Download all playlists of YouTube channel/user keeping each playlist in separate directory:

`yt-dlp -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/user/TheLinuxFoundation/playlists</span>`"`

- Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home:

`yt-dlp -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/MyVideos</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.udemy.com/java-tutorial</span>`"`

- Download entire series season keeping each series and each season in separate directory under C:/MyVideos:

`yt-dlp -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:/MyVideos</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://videomore.ru/kino_v_detalayah/5_sezon/367617</span>`"`
