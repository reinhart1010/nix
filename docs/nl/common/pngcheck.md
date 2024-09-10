---
layout: page
title: common/pngcheck (Nederlands)
description: "Gedetailleerde informatie over en verifiëren van PNG-, JNG- en MNG-bestanden."
content_hash: d8d72854d5500bb52fa48218c4ae10154e51d4fa
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/pngcheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pngcheck

Gedetailleerde informatie over en verifiëren van PNG-, JNG- en MNG-bestanden.
Meer informatie: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Toon een samenvatting van een afbeelding (breedte, hoogte, en kleurdiepte):

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>

- Toon informatie over een afbeelding met gekleurde ([c]) uitvoer:

`pngcheck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>

- Toon gedetailleerde ([v]) informatie over een afbeelding:

`pngcheck -cvt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>

- Ontvang een afbeelding van `stdin` en toon gedetailleerde informatie:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>` | pngcheck -cvt`

- Zoek ([s]) naar PNG-bestanden binnen een specifiek bestand en toon informatie:

`pngcheck -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>

- Zoek naar PNG's binnen een ander bestand en e[x]tracteer ze:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.png</span>
