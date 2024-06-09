---
layout: page
title: common/magick-import (Nederlands)
description: "Leg een deel of het geheel van een X server scherm vast en sla de afbeelding op in een bestand."
content_hash: 09c811edc926cfe45cd71f163a789236158e169d
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/magick-import.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick import

Leg een deel of het geheel van een X server scherm vast en sla de afbeelding op in een bestand.
Bekijk ook: `magick`.
Meer informatie: <https://imagemagick.org/script/import.php>.

- Leg het hele X server scherm vast in een PostScript bestand:

`magick import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ps</span>

- Leg de inhoud van een extern X server scherm vast in een PNG afbeelding:

`magick import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externe_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scherm</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.png</span>

- Leg een specifiek venster vast op basis van zijn ID zoals weergegeven door `xwininfo` in een JPEG-afbeelding:

`magick import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.jpg</span>
