---
layout: page
title: linux/pngcheck (Nederlands)
description: "Forensische tool voor het valideren van de integriteit van PNG-gebaseerde (PNG, JNG, MNG) afbeeldingsbestanden."
content_hash: d6f7293501392c7db3a65342c7fbb784cd59a54a
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/linux/pngcheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pngcheck

Forensische tool voor het valideren van de integriteit van PNG-gebaseerde (PNG, JNG, MNG) afbeeldingsbestanden.
Kan ook ingebedde afbeeldingen en tekst uit een bestand extraheren.
Meer informatie: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Controleer de integriteit van een afbeeldingsbestand:

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.png</span>

- Controleer het bestand met [v]erbeterde en gekleurde ([c]) uitvoer:

`pngcheck -vc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.png</span>

- Toon de inhoud van [t]ekstfragmenten en zoek ([s]) naar PNG's binnen een specifiek bestand:

`pngcheck -ts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.png</span>

- Zoek naar en e[x]tracteer ingebedde PNG's binnen een specifiek bestand:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.png</span>
