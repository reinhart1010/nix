---
layout: page
title: common/du (Deutsch)
description: "Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln."
content_hash: 3f7a7eec4d3de12b05fcd7dd1076c8efb28b67c6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

Disk usage: Plattenplatzverbrauch von Dateien und Verzeichnissen ermitteln.
Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

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

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
