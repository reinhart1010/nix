---
layout: page
title: common/ffprobe (Deutsch)
description: "Multimedia Stream Analysierer."
content_hash: 73b97cc3a506b6ecd146545fd166a07554275922
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/ffprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffprobe

Multimedia Stream Analysierer.
Weitere Informationen: <https://ffmpeg.org/ffprobe.html>.

- Zeige alle verfügbaren Stream-Informationen einer Medien-Datei an:

`ffprobe -v error -show_streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die Spieldauer an:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die Bildfrequenz eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die Breite (width) oder Höhe (height) eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die durchschnittliche Bitrate eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>
