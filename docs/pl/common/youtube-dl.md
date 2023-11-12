---
layout: page
title: common/youtube-dl (polski)
description: "Pobieraj wideo i audio z YouTube i podobnych portali."
content_hash: 725187e060d93074dde806a88854256261085422
last_modified_at: 2023-11-12
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
  - title: italiano version
    url: /it/common/youtube-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# youtube-dl

Pobieraj wideo i audio z YouTube i podobnych portali.
Więcej informacji: <http://rg3.github.io/youtube-dl/>.

- Pobierz plik wideo lub wszystkie pliki z playlisty:

`youtube-dl '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Wypisz wszystkie formaty dostępne dla filmu lub playlisty:

`youtube-dl --list-formats '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Pobierz wideo lub playlistę w wybranej jakości:

`youtube-dl --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best[height<=480]</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Pobierz audio z wideo w formacie mp3:

`youtube-dl -x --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Pobierz wideo ze ścieżką audio złączone w jednym pliku w najlepszej dostępnej jakości:

`youtube-dl -f bestvideo+bestaudio '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Pobierz wideo jako pliki MP4 i nazwij wedle schematu:

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Pobierz plik razem z napisami:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Pobierz ścieżkę dźwiękową ze wszystkich filmów z playlisty:

`youtube-dl -i --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url_playlisty</span>`'`
