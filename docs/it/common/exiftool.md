---
layout: page
title: common/exiftool (italiano)
description: "Leggi e scrivi metadati nei file."
content_hash: c1a6076e2a53c2fc2e48a082ab9c325d26b9357a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/exiftool.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># exiftool

Leggi e scrivi metadati nei file.
Maggiori informazioni: <https://exiftool.org>.

- Rimuovi tutti i metadati EXIF dai file specificati:

`exiftool -All= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Muovi avanti di 1 ora la data in cui sono state scattate tutte le foto contenute in una directory:

`exiftool "-AllDates+=0:0:0 1:0:0" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Muovi indietro di 1 giorno e 2 ore la data in cui sono state scattate tutte le immagini JPEG:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Cambia solo il campo `DateTimeOriginal` sottraendo 1.5 ore e non tenere file di backup:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Rinomina ricorsivamente tutti i file JPEG in una directory in base al campo `DateTimeOriginal`:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` -r -ext jpg`
