---
layout: page
title: common/pcdovtoppm (Nederlands)
description: "Maak een indexafbeelding voor een fotocd op basis van het overzichtsbestand."
content_hash: f0a29e74774748b1334dc1f382986c51b4c8dfa4
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pcdovtoppm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pcdovtoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcdovtoppm

Maak een indexafbeelding voor een fotocd op basis van het overzichtsbestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Maak een PPM-indexafbeelding van een PCD-overzichtsbestand:

`pcdovtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Specificeer de [m]aximale breedte van de uitvoer-afbeelding en de maximale grootte ([s]) van elke afbeelding die in de uitvoer wordt opgenomen:

`pcdovtoppm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grootte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Specificeer het maximale [a]antal afbeeldingen en het maximale aantal kleuren ([c]):

`pcdovtoppm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_afbeeldingen</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>

- Gebruik het gespecificeerde lettertype ([f]) voor annotaties en kleur de achtergrond [w]it:

`pcdovtoppm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lettertype</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pcd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ppm</span>
