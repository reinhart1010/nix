---
layout: page
title: common/ffmpeg (italiano)
description: "Tool per convertire audio e video."
content_hash: a9371d4ddf4402b5021f33953a5c590d4f3bd062
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ffmpeg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffmpeg.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ffmpeg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ffmpeg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffmpeg

Tool per convertire audio e video.
Maggiori informazioni: <https://ffmpeg.org>.

- Estrai l'audio da un video e salvalo come MP3:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio</span>`.mp3`

- Converti i fotogrammi di un video o una GIF in una serie di immagini numerate:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mpg|video.gif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foto_%d.png</span>

- Sequenzia immagini numerate (`foto_1.jpg`, `foto_2.jpg`, ecc) per creare un video o una GIF:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frame_%d.jpg</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mpg|video.gif</span>

- Estrai un singolo fotogramma da un video al timestamp mm:ss e salvalo come immagine di dimensioni 128x128:

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -frames 1 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">128x128</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Taglia un video da un momento iniziale mm:ss a un momento finale mm:ss (rimuovi la flag -to per tagliare fino alla fine):

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm2:ss2</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Converti un video AVI a MP4. Audio AAC a 128kbit, video h264 a CRF 23:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.mp4`

- Effettua un remux di un video MKV a MP4 senza re-encodare gli stream audio o video:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.mkv -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.mp4`

- Converti un video MP4 a codec VP9. Per ottenere la migliore qualità possibile, usa un valore di CRF (consigliabile tra 15-35) e -b:video DEVE essere 0:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.mp4 -codec:video libvpx-vp9 -crf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -b:video 0 -codec:audio libopus -vbr on -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.webm`
