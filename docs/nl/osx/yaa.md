---
layout: page
title: osx/yaa (Nederlands)
description: "Maak en beheer YAA-archieven."
content_hash: e4573f3448c6977635118577fd9c605acc63bb30
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/yaa.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yaa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaa

Maak en beheer YAA-archieven.
Meer informatie: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Maak een archief van een map:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.yaa</span>

- Maak een archief van een bestand:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.yaa</span>

- Pak een archief uit naar de huidige map:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archive_file.yaa</span>

- Lijst de inhoud van een archief op:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archive_file.yaa</span>

- Maak een archief met een specifiek compressie-algoritme:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algoritme</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.yaa</span>

- Maak een archief met een blokgrootte van 8 MB:

`yaa archive -b 8m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.yaa</span>
