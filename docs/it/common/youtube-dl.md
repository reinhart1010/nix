---
layout: page
title: common/youtube-dl (italiano)
description: "Scarica video da YouTube ed altri siti web."
content_hash: 0ab8687daf31e8b1ae7cf05049a04bba8cac2851
last_modified_at: 2023-12-29
related_topics:
  - title: català version
    url: /ca/common/youtube-dl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/youtube-dl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/youtube-dl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/youtube-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# youtube-dl

Scarica video da YouTube ed altri siti web.
Maggiori informazioni: <http://rg3.github.io/youtube-dl/>.

- Scarica un video od una playlist:

`youtube-dl '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Elenca tutti i formati in cui un video od una playlist sono disponibili:

`youtube-dl --list-formats '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Scarica un video od una playlist con la qualità specificata:

`youtube-dl --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best[height<=480]</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Scarica l'audio di un video e lo converte in file MP3:

`youtube-dl -x --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Scarica l'audio di migliore qualità e il video di migliore qualità e li unisce:

`youtube-dl -f bestvideo+bestaudio '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Scarica una playlist di video e li salva come file MP4 dai nomi personalizzati:

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(title)s di %(uploader)s del %(upload_date)s in %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Scarica, assieme al video, i sottotitoli in una lingua specificata:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">it</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Scarica una playlist, ne estrae l'audio e lo salva in formato mp3:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_della_playlist</span>`'`
