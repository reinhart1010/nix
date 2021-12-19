---
layout: page
title: common/id3tag (italiano)
description: "Strumento per leggere, scrivere, e manipolare i tag (etichette) ID3v1 e ID3v2 di file MP3."
content_hash: cc8ccc5017bad08ae70320b4acf9498f4b50bb7a
related_topics:
  - title: English version
    url: /en/common/id3tag.html
    icon: bi bi-globe
---
# id3tag

Strumento per leggere, scrivere, e manipolare i tag (etichette) ID3v1 e ID3v2 di file MP3.
Maggiori informazioni: <https://manned.org/id3tag>.

- Imposta l'etichetta dell'artista e del titolo in un file MP3:

`id3tag --artist=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artista</span>` --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titolo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.mp3</span>

- Imposta il titolo dell'album di tutti i file MP3 nella cartella corrente:

`id3tag --album=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">album</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- Fornisce altro aiuto:

`id3tag --help`
