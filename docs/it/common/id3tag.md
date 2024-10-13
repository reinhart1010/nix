---
layout: page
title: common/id3tag (italiano)
description: "Strumento per leggere, scrivere, e manipolare i tag (etichette) ID3v1 e ID3v2 di file MP3."
content_hash: 71f8490bec702e53f7da7126823f37707b2aa9c7
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/id3tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# id3tag

Strumento per leggere, scrivere, e manipolare i tag (etichette) ID3v1 e ID3v2 di file MP3.
Maggiori informazioni: <https://manned.org/id3tag>.

- Imposta l'etichetta dell'artista e del titolo in un file MP3:

`id3tag --artist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artista</span>` --song `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titolo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.mp3</span>

- Imposta il titolo dell'album di tutti i file MP3 nella directory corrente:

`id3tag --album `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">album</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- Fornisce altro aiuto:

`id3tag --help`
