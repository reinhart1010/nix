---
layout: page
title: common/ffmpeg (português (Brasil))
description: "Ferramenta de conversão de vídeo."
content_hash: 649e414e8f28a81fd5264f7fd434f76edf4ccbe3
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/common/ffmpeg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffmpeg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffmpeg.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ffmpeg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffmpeg

Ferramenta de conversão de vídeo.
Mais informações: <https://ffmpeg.org>.

- Extrai o som de um vídeo e salva-o como MP3:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo.mp4</span>` -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/som.mp3</span>

- Transcodifica um arquivo FLAC to formato de CD Red Book (44100kHz, 16bit):

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/audio_de_entrada.flac</span>` -ar 44100 -sample_fmt s16 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/audio_de_saida.wav</span>

- Salva um vídeo como GIF, escalando a altura para 1000px e definindo a taxa de quadros para 15:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo.mp4</span>` -vf 'scale=-1:1000' -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/saída.gif</span>

- Combina imagens numeradas (`quadro_1.jpg`, `quadro_2.jpg`, etc) em um vídeo ou GIF:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/quadro_%d.jpg</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vídeo.mpg|vídeo.gif</span>

- Corta um vídeo de um dado tempo inicial mm:ss até um tempo final mm2:ss2 (omita a opção -to para cortar o vídeo até o final):

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_entrada.mp4</span>` -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm2:ss2</span>` -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_saída.mp4</span>

- Converte um vídeo AVI para MP4. AAC Áudio @ 128kbit, h264 Vídeo @ CRF 23:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_entrada</span>`.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_saída</span>`.mp4`

- Remixa um vídeo MKV para MP4 sem recodificar o áudio ou o vídeo:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_entrada</span>`.mkv -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_saída</span>`.mp4`

- Converte um vídeo MP4 para o codec VP9. Para a melhor qualidade, use um valor CRF (faixa recomendada 15-35) e -b:v DEVE ser 0:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_entrada</span>`.mp4 -codec:v libvpx-vp9 -crf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -b:v 0 -codec:a libopus -vbr on -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_threads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/vídeo_saída</span>`.webm`
