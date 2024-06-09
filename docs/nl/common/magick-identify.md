---
layout: page
title: common/magick-identify (Nederlands)
description: "Beschrijf het formaat en eigenschappen van afbeeldingen."
content_hash: d5450ecb2a0a12c41d8094308accf82903e92af5
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/magick-identify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick identify

Beschrijf het formaat en eigenschappen van afbeeldingen.
Bekijk ook: `magick`.
Meer informatie: <https://imagemagick.org/script/identify.php>.

- Beschrijf het formaat en basis eigenschappen van een afbeelding:

`magick identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding</span>

- Beschrijf het formaat en uitgebreide eigenschappen van een afbeelding:

`magick identify -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding</span>

- Verzamel de dimensies van alle JPEG bestanden in de huidige map en sla ze op naar een CSV-bestand:

`magick identify -format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%f,%w,%h\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestandslijst.csv</span>
