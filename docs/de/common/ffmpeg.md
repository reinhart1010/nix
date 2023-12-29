---
layout: page
title: common/ffmpeg (Deutsch)
description: "Programm zum konvertieren von Videos."
content_hash: 4a7b8e995d580b71b03e9ff36d1e22af7df84baa
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/ffmpeg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffmpeg.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ffmpeg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ffmpeg.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ffmpeg

Programm zum konvertieren von Videos.
Weitere Informationen: <https://ffmpeg.org>.

- Extrahiere den Ton eines Videos und speichere ihn als MP3:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/video.mp4</span>` -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/audio</span>`.mp3`

- Kombiniere nummerierte Bilder (`frame_1.jpg`, `frame_2.jpg`, etc) in ein Video oder Gif:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/frame_%d.jpg</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mpg|video.gif</span>

- Extrahiere einen einzelnen Frame von einem Video bei mm:ss and speichere als 128x128 Bild:

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/video.mp4</span>` -frames 1 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">128x128</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>

- Trimme ein Video von mm:ss bis mm2:ss2 (Ohne -to bis zum Ende des Videos):

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm2:ss2</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/video/video.mp4</span>` -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output.mp4</span>

- Konvertiere ein AVI Video zu MP4. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/input_video</span>`.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output_video</span>`.mp4`

- Remuxe ein MKV Video zu MP4 ohne Audio oder Video streams neu zu codieren:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/input_video</span>`.mkv -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output_video</span>`.mp4`

- Konvertiere ein MP4 video zu VP9. Für beste Qualität, nutze einen CRF Wert von 15 bis 35 und -b:v MUSS 0 sein:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/input_video</span>`.mp4 -codec:v libvpx-vp9 -crf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -b:v 0 -codec:a libopus -vbr on -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thread_anzahl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output_video</span>`.webm`
