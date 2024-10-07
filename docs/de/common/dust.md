---
layout: page
title: common/dust (Deutsch)
description: "Dust gib einen sofortigen Überblick, welche Verzeichnisse Festplatten Speicherplatz benutzen."
content_hash: 479301c97c2b74ba9c8036fecd0d03546e0c1737
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/dust.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dust.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dust

Dust gib einen sofortigen Überblick, welche Verzeichnisse Festplatten Speicherplatz benutzen.
Weitere Informationen: <https://github.com/bootandy/dust>.

- Informationen für das aktuelle Verzeichnis anzeigen:

`dust`

- Informationen für eine durch Leerzeichen getrennte Liste von Verzeichnissen anzeigen:

`dust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis2</span>

- Zeige 30 Verzeichnisse an (Standardwert: 21):

`dust --number-of-lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Zeigt Informationen für das aktuelle Verzeichnis an, bis zu 3 Ebenen tief:

`dust --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Die größten Verzeichnisse in absteigender Reihenfolge oben anzeigen:

`dust --reverse`

- Alle Dateien und Verzeichnisse mit einem bestimmten Namen ignorieren:

`dust --ignore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_oder_verzeichnis_name</span>

- Keine Prozentbalken und Prozente anzeigen:

`dust --no-percent-bars`
