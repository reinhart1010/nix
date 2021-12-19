---
layout: page
title: common/nodemon (Deutsch)
description: "Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden."
content_hash: c2ff812d20b907bba9ea2ea0ef7b0ba433395e99
related_topics:
  - title: English version
    url: /en/common/nodemon.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nodemon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nodemon

Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden.
Weitere Informationen: <https://nodemon.io>.

- Führe die angegebene Datei aus und warte auf Änderungen:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.js</span>

- Manueller Neustart von Nodemon (beachte, dass Nodemon dabei aktiv sein muss):

`rs`

- Ignoriere bestimmte Dateien:

`nodemon --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Übergib Argumente an die Node Applikation:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumente</span>

- Führe Nicht-Node Skripte aus:

`nodemon --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python --verbose</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.py</span>
