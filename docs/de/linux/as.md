---
layout: page
title: linux/as (Deutsch)
description: "Portabler GNU assembler."
content_hash: 16d17a4608618387580e4e26b3c9de2a2c97d59c
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/as.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Portabler GNU assembler.
Hauptsächlich beabsichtigt um output von `gcc` für `ld` vorzubereiten.
Weitere Informationen: <https://manned.org/as>.

- Assemble eine Datei und schreibe den Output in eine in `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.s</span>

- Assemble den Output einer gegebenen Datei:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/out.o</span>

- Generiere den Output schneller indem Leerzeichen und Kommentare nicht verarbeitet werden. (Sollte nur für vertrauenswürdige Compiler benutzt werden):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.s</span>

- Inkludiere einen gegebenen Pfad in der Liste von Verzeichnissen für die Suche nach Dateien:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.s</span>
