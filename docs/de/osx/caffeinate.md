---
layout: page
title: osx/caffeinate (Deutsch)
description: "Hindert den Mac daran, in den Schlaf-Modus zu gehen."
content_hash: 7286c98f9b01ce885bc35c0b7e0225cb8e9917cd
last_modified_at: 2023-11-12
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
Weitere Informationen: <https://ss64.com/osx/caffeinate.html>.

- Halte den Mac für 1 Stunde (3600 Sekunden) wach:

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Halte den Mac wach, bis ein bestimmter Befehl abgeschlossen ist:

`caffeinate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Halte den Mac wach, bis `caffeinate` durch Cmd-C beendet wird:

`caffeinate -i`
