---
layout: page
title: common/dust (Deutsch)
description: "Dust gib einen sofortigen Überblick, welche Verzeichnisse Festplatten Speicherplatz benutzen."
content_hash: b23702cd2e5d8c113aedbc9e3c17c95e3ed7e997
last_modified_at: 2024-10-13
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

`dust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis1 pfad/zu/verzeichnis2 ...</span>

- Zeige 30 Verzeichnisse an (Standardwert: 21):

`dust --number-of-lines 30`

- Zeigt Informationen für das aktuelle Verzeichnis an, bis zu 3 Ebenen tief:

`dust --depth 3`

- Die größten Verzeichnisse in absteigender Reihenfolge oben anzeigen:

`dust --reverse`

- Alle Dateien und Verzeichnisse mit einem bestimmten Namen ignorieren:

`dust --ignore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_oder_verzeichnis_name</span>

- Keine Prozentbalken und Prozente anzeigen:

`dust --no-percent-bars`
