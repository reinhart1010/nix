---
layout: page
title: linux/xwinwrap (português (Brasil))
description: "Usa um reprodutor de vídeo ou um programa como plano de fundo."
content_hash: b86aca7f0b3e473f6fa174b558a67d0b41dcccad
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xwinwrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwinwrap

Usa um reprodutor de vídeo ou um programa como plano de fundo.
Mais informações: <https://github.com/ujjwal96/xwinwrap>.

- Reproduz um vídeo usando mpv:

`xwinwrap -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/video.mp4</span>

- Reproduz um vídeo em tela cheia usando mpv:

`xwinwrap -b -nf -fs -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/video.mp4</span>

- Reproduz um vídeo usando mpv com 80% de opacidade:

`xwinwrap -b -nf -ov -o 0.8 --- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/video.mp4</span>

- Reproduz um vídeo usando mpv em um segundo monitor 1600x900 com 1920 de distância do eixo X:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/video.mkv</span>
