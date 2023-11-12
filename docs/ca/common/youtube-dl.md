---
layout: page
title: common/youtube-dl (català)
description: "Descarrega videos de YouTube i altres pàgines web."
content_hash: f4bf17c9cdb1bb14048b5bd51e9d538861c0f9f4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/youtube-dl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/youtube-dl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/youtube-dl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/youtube-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# youtube-dl

Descarrega videos de YouTube i altres pàgines web.
Més informació: <http://rg3.github.io/youtube-dl/>.

- Descarrega un vídeo o playlist:

`youtube-dl '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Llista tots els formats en el que es troba disponible un vídeo o playlist:

`youtube-dl --list-formats '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Descarrega un vídeo o playlist en una qualitat específica:

`youtube-dl --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best[height<=480]</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Descarrega l'àudio d'un vídeo i converteix-lo a MP3:

`youtube-dl -x --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Descarrega l'àudio i el vídeo de major qualitat i fusiona'ls:

`youtube-dl -f bestvideo+bestaudio '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Descarrega vídeo(s) com a fitxers MP4 amb un nom específic:

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Descarrega els subtítols d'un llenguatge en concret amb el vídeo:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Descarrega una playlist i extreu-ne els MP3s:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_to_playlist</span>
