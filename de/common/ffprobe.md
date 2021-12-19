---
layout: page
title: common/ffprobe (Deutsch)
description: "Multimedia Stream Analysierer."
content_hash: 62151f7ff1400541e329f2090ec0aa08b2f25c08
related_topics:
  - title: English version
    url: /en/common/ffprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffprobe.html
    icon: bi bi-globe
---
# ffprobe

Multimedia Stream Analysierer.
Weitere Informationen: <https://ffmpeg.org/ffprobe.html>.

- Zeige alle verfügbaren Stream-Informationen einer Medien-Datei an:

`ffprobe -v error -show_entries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige Spieldauer an:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die Bildfrequenz eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die Breite (width) oder Höhe (height) eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>

- Zeige die durchschnittliche Bitrate eines Videos an:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.mp4</span>
