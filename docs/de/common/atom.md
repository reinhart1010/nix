---
layout: page
title: common/atom (Deutsch)
description: "Ein plattformübergreifender erweiterbarer Texteditor."
content_hash: f7639acfe3ea3660df850ef234a4c8f03d6e5456
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atom

Ein plattformübergreifender erweiterbarer Texteditor.
Erweiterungen werden durch `apm` verwaltet.
Weitere Informationen: <https://atom.io/>.

- Öffne eine Datei oder ein Verzeichnis:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Öffne eine Datei oder ein Verzeichnis in einem neuen Fenster:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Öffne eine Datei oder ein Verzeichnis in einem vorhandenen Fenster:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Starte Atom im sicheren Modus (Es werden keine zusätzlichen Pakete geladen):

`atom --safe`

- Verhindert, dass sich Atom in den Hintergrund absetzt und hält es mit dem Terminal verbunden:

`atom --foreground`

- Wartet, bis Atom geschlossen wurde, bevor die Eingabeaufforderung wieder aktiv wird (Nützlich als `git commit` Editor):

`atom --wait`
