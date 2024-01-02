---
layout: page
title: common/youtube-dl (polski)
description: "Pobieraj wideo i audio z YouTube i podobnych portali."
content_hash: d15810889f2e979a46414cbffcb1e3dd0a9a80a3
last_modified_at: 2024-01-02
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

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Pobierz plik razem z napisami:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Pobierz playlistę i wyodrębnij z niej pliki MP3:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url_playlisty</span>`'`
