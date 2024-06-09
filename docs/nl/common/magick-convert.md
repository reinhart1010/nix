---
layout: page
title: common/magick-convert (Nederlands)
description: "Converteer tussen afbeeldingsformaten, schaal, voeg samen, maak afbeeldingen en nog veel meer."
content_hash: 7abbda74a48be031cf1883fa36590936c21afc0b
last_modified_at: 2024-06-09
related_topics:
  - title: Deutsch version
    url: /de/common/magick-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/magick-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/magick-convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/magick-convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick convert

Converteer tussen afbeeldingsformaten, schaal, voeg samen, maak afbeeldingen en nog veel meer.
Let op: deze tool (voorheen `convert`) is vervangen door `magick` in ImageMagick 7+.
Meer informatie: <https://imagemagick.org/script/convert.php>.

- Converteer een afbeelding van JPEG naar PNG:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.png</span>

- Schaal een afbeelding naar 50% van zijn originele grootte:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.png</span>

- Schaal een afbeelding en behoud de originele aspect ratio tot een maximale dimensie van 640x480:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.png</span>

- Schaal een afbeelding zodat deze een gespecificeerde bestandsgrootte heeft:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` -define jpeg:extent=512kb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.jpg</span>

- Verticaal/horizontaal toevoegen van afbeeldingen:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-append|+append</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.png</span>

- Maak een GIF van een series van afbeeldingen met 100ms pauze ertusen:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/animation.gif</span>

- Maak een afbeelding met niets anders dan een volledig rode achtergrond:

`magick convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>

- Maak een favicon van verschillende afbeeldingen met verschillende groottes:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/favicon.ico</span>
