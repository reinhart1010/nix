---
layout: page
title: common/mpv (português (Brasil))
description: "Um tocador de vídeo/audio baseado no MPlayer."
content_hash: f18da1bd86fa5009a5476a33a51e91ca4ae0250f
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/mpv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mpv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpv

Um tocador de vídeo/audio baseado no MPlayer.
Mais informações: <https://mpv.io>.

- Toca um vídeo ou áudio de uma URL ou arquivo:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|caminho/para/arquivo</span>`'`

- Avança/retrocede 5 segundos:

`LEFT <or> RIGHT`

- Avança/retrocede 1 minuto:

`DOWN <or> UP`

- Aumenta ou diminui a velocidade de reprodução em 10%:

`[ <or> ]`

- Captura a imagem atual (salva em `./mpv-shotNNNN.jpg` por padrão):

`s`

- Toca um arquivo em uma velocidade especificada (1 por padrão):

`mpv --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.01..100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Toca um arquivo usando um perfil definido no arquivo `mpv.conf`:

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_perfil</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Mostra a saída da webcam ou de outro dispositivo de entrada de vídeo:

`mpv /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video0</span>
