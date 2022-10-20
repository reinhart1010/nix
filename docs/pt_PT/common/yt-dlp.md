---
layout: page
title: common/yt-dlp (português (Portugal))
description: "Um fork do youtube-dl com funcionalidades e correções adicionais."
content_hash: edfc68a8f26478868f338d2b2601c8027a197c9e
related_topics:
  - title: English version
    url: /en/common/yt-dlp.html
    icon: bi bi-globe
---
# yt-dlp

Um fork do youtube-dl com funcionalidades e correções adicionais.
Descarrega vídeos do YouTube e de outros websites.
Mais informações: <https://github.com/yt-dlp/yt-dlp>.

- Descarregar um vídeo ou playlist (com as opções predefinidas):

`yt-dlp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Descarregar um vídeo num formato específico, neste caso o melhor vídeo mp4 disponível (a predefinição é "bv\*+ba/b"):

`yt-dlp --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Extrair áudio de vídeos (requer o `ffmpeg` ou o `ffprobe`):

`yt-dlp --extract-audio "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Especificar o formato de áudio extraído (a predefinição é "best"):

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Especificar a qualidade do áudio extraído, entre 0 (melhor) e 10 (pior), sendo 5 a predefinição:

`yt-dlp --extract-audio --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` --audio-quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`"`

- Descarregar todas as playlists de um canal ou utilizador do YouTube, mantendo cada playlist num diretório separado:

`yt-dlp -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(uploader)s/%(playlist)s/%(indice_playlist)s - %(titulo)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/user/TheLinuxFoundation/playlists</span>`"`

- Descarregar um curso do Udemy, mantendo cada capítulo num diretório em separado, dentro do diretório "MyVideos" na home do utilizador:

`yt-dlp -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_passe</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/MyVideos</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist)s/%(numero_capitulo)s - %(capitulo)s/%(titulo)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.udemy.com/java-tutorial</span>`"`

- Descarregar temporadas completas de séries, mantendo cada série e cada temporada num diretório separado, em C:\MyVideos:

`yt-dlp -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:/MyVideos</span>`" -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(serie)s/%(numero_temporada)s - %(temporada)s/%(numero_episodio)s - %(episodio)s.%(ext)s</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://videomore.ru/kino_v_detalayah/5_sezon/367617</span>`"`
