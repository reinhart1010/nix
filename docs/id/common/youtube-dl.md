---
layout: page
title: common/youtube-dl (Indonesia)
description: "Unduh video dari YouTube dan situs web lain."
content_hash: b6d9a365c911f8e810f9ec8bf67580b913004dec
last_modified_at: 2024-01-02
related_topics:
  - title: català version
    url: /ca/common/youtube-dl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/youtube-dl.html
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

Unduh video dari YouTube dan situs web lain.
Informasi lebih lanjut: <http://rg3.github.io/youtube-dl/>.

- Mengunduh sebuah video atau daftar putar:

`youtube-dl '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Tampilkan daftar format yang tersedia untuk video atau daftar putar:

`youtube-dl --list-formats '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Mengunduh video atau daftar putar dengan kualitas tertentu:

`youtube-dl --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best[height<=480]</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=oHg5SJYRHA0</span>`'`

- Mengunduh audio dari video dan ubah menjadi MP3:

`youtube-dl -x --audio-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Mengunduh video dan audio dengan kualitas terbaik lalu gabungkan:

`youtube-dl -f bestvideo+bestaudio '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Mengunduh satu atau beberapa video sebagai file MP4 dengan nama tertentu:

`youtube-dl --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp4</span>` -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%(playlist_index)s-%(title)s oleh %(uploader)s pada %(upload_date)s di dalam %(playlist)s.%(ext)s</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`'`

- Mengunduh video bersama dengan subtitle bahasa tertentu:

`youtube-dl --sub-lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` --write-sub '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=Mwa0_nE9H7A</span>`'`

- Mengunduh daftar putar dan ekstrak MP3 darinya:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_to_playlist</span>`'`
