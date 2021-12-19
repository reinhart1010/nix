---
layout: page
title: common/exiftool (italiano)
description: "Leggi e scrivi metadati nei file."
content_hash: cfc0ad61414a3ef2d94f42bafc78d6e5718d3654
related_topics:
  - title: English version
    url: /en/common/exiftool.html
    icon: bi bi-globe
---
# exiftool

Leggi e scrivi metadati nei file.
Maggiori informazioni: <https://exiftool.org>.

- Rimuovi tutti i metadati EXIF dai file specificati:

`exiftool -All= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Muovi avanti di 1 ora la data in cui sono state scattate tutte le foto contenute in una directory:

`exiftool "-AllDates+=0:0:0 1:0:0" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory</span>

- Muovi indietro di 1 giorno e 2 ore la data in cui sono state scattate tutte le immagini JPEG:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Cambia solo il campo `DateTimeOriginal` sottraendo 1.5 ore e non tenere file di backup:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Rinomina ricorsivamente tutti i file JPEG in una directory in base al campo `DateTimeOriginal`:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory</span>` -r -ext jpg`
