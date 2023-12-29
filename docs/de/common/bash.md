---
layout: page
title: common/bash (Deutsch)
description: "Bourne-Again SHell."
content_hash: 009b32ff5ffa459e40fee7b222c5812e2c6f1a86
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bash

Bourne-Again SHell.
`sh`-kompatibler Kommandozeilen-Interpreter.
Weitere Informationen: <https://www.gnu.org/software/bash/>.

- Interaktive Shell starten:

`bash`

- Führe einen Befehl aus:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`"`

- Führe Befehle aus einer Datei aus:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.sh</span>

- Führe Befehle aus einer Datei aus und protokolliere alle ausgeführten Befehle an das Terminal:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.sh</span>

- Führe Befehle aus einer Datei aus und stoppe beim ersten Fehler:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.sh</span>

- Führe Befehle von `stdin` aus:

`bash -s`

- Gib die Version von bash aus (verwende `echo $BASH_VERSION`, um nur die Versionszeichenkette anzuzeigen):

`bash --version`
