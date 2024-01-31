---
layout: page
title: osx/caffeinate (Deutsch)
description: "Hindert den Mac daran, in den Schlaf-Modus zu gehen."
content_hash: f35ae7726dd2035c9be8d7b82fdf63baad074d11
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

Hindert den Mac daran, in den Schlaf-Modus zu gehen.
Weitere Informationen: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Halte den Mac für 1 Stunde (3600 Sekunden) wach:

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Halte den Mac wach, bis ein bestimmter Befehl abgeschlossen ist:

`caffeinate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Halte den Mac wach, bis `caffeinate` durch Cmd-C beendet wird:

`caffeinate -i`
