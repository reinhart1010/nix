---
layout: page
title: common/tar (Deutsch)
description: "Archivierungstool."
content_hash: d5d71a7cdf1848bee173fafb8b1f9aa6a801e92e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tar.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tar

Archivierungstool.
Häufig kombiniert mit anderen Methoden zur Komprimierung, wie gzip oder bzip2.
Weitere Informationen: <https://www.gnu.org/software/tar>.

- Erstelle ein Archiv von Dateien:

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei3</span>

- Erstelle ein mit gzip komprimiertes Archiv:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei3</span>

- Erstelle ein mit gzip komprimiertes Archiv mit relativen Pfaden:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel.tar.gz</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis/</span>` .`

- Extrahiere ein (komprimiertes) Archiv in das derzeitige Verzeichnis:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelle.tar[.gz|.bz2|.xz]</span>

- Extrahiere ein Archiv in ein Verzeichnis:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelle.tar</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verzeichnis</span>

- Erstelle ein komprimiertes Archiv und benutze den die Dateiendung des Archivs um die Kompressionsmethode zu wählen:

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei3</span>

- Führe die Inhalte eines tar Archivs auf:

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelle.tar</span>

- Extrahiere Dateien die mit einem Muster übereinstimmen:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelle.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
