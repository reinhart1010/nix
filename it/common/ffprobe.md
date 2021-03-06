---
layout: page
title: common/ffprobe (italiano)
description: "Analizzatore di flussi multimediali."
content_hash: 0bea256859cb7f66d9c4f414dfaca8507fa35d4f
related_topics:
  - title: Deutsch version
    url: /de/common/ffprobe.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffprobe.html
    icon: bi bi-globe
---
# ffprobe

Analizzatore di flussi multimediali.
Maggiori informazioni: <https://ffmpeg.org/ffprobe.html>.

- Visualizza tutte le informazioni disponibili sui flussi di un file multimediale (audio, video, immagini, etc):

`ffprobe -v error -show_entries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.mp4</span>

- Visualizza la durata del contenuto:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.mp4</span>

- Visualizza la frequenza dei fotogrammi di un video:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>

- Visualizza la larghezza o l'altezza di un video:

`ffprobe -v error -select_streams v:0 -show_entries stream=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>

- Visualizza il bit-rate medio di un video:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>
