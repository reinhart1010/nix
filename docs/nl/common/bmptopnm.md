---
layout: page
title: common/bmptopnm (Nederlands)
description: "Converteer een BMP bestand naar een PBM, PGM of PNM afbeelding."
content_hash: 7b7fd8e21e4c16edca4ecd6cee0fe2f1c4529b8e
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/common/bmptopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmptopnm

Converteer een BMP bestand naar een PBM, PGM of PNM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/bmptopnm.html>.

- Genereer de PBM, PGM of PNM afbeelding als output, vanuit een Windows of OS/2 BMP afbeelding als input:

`bmptopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.bmp</span>

- Rapporteer de inhoud van een BMP header naar `stderr`:

`bmptopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.bmp</span>

- Toon de versie:

`bmptopnm -version`
