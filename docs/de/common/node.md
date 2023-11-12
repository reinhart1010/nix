---
layout: page
title: common/node (Deutsch)
description: "Server-seitige JavaScript Plattform (Node.js)."
content_hash: 19000060cc252c1a271c4af4e510f98163f15f31
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># node

Server-seitige JavaScript Plattform (Node.js).
Weitere Informationen: <https://nodejs.org>.

- Führe eine JavaScript Datei aus:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Starte eine REPL (Interaktive Shell):

`node`

- Evaluiere als Argument übergebenen JavaScript Code:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Evaluierung und Ausgabe des Ergebnisses. Nützlich, um die Versionen der Abhängigkeiten von Node zu sehen:

`node -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.versions</span>`"`

- Aktiviere Inspector und pausiere die Ausführung bis sich ein Debugger verbindet sobald der Quellcode vollständig geparsed ist:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
