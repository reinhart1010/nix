---
layout: page
title: common/du (Deutsch)
description: "Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln."
content_hash: fee933e6f4e24aac01d5bb0bcfdae12ca0a8d192
related_topics:
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
---
# du

Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln.
Weitere Informationen: <https://www.gnu.org/software/coreutils/du>.

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in den gegebenen Einheiten (B/KiB/MiB) auf:

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Liste die Größe von Verzeichnissen und Unterverzeichnissen in menschenlesbaren Einheiten auf (d.h. automatische Auswahl der geeigneten Einheit für jede Größe):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Zeige die Größe eines einzelnen Verzeichnisses in menschenlesbaren Einheiten:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Liste die Größe von Verzeichnissen und Unterverzeichnissen und aller ihrer Dateien in menschenlesbaren Einheiten auf:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Liste die menschenlesbaren Größen eines Verzeichnisses und aller Unterverzeichnisse, bis zu einer Tiefe von `N` Ebenen:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Liste die menschenlesbare Größe aller `.jpg`-Dateien in Unterverzeichnissen des aktuellen Verzeichnisses auf und zeige am Ende die kumulierte Gesamtsumme an:

`du -ch */*.jpg`
