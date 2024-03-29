---
layout: page
title: common/zsh (Deutsch)
description: "Z SHell."
content_hash: 033badbec4c13d8bb295fc23fe09909fd11717a9
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zsh

Z SHell.
Mit `bash` und `sh` kompatible Eingabeaufforderung.
Weitere Informationen: <https://www.zsh.org>.

- Starte eine interaktive Eingabeaufforderung:

`zsh`

- Führe Parameter als Befehl aus:

`zsh -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Führe Befehle aus einem Skript aus:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript</span>

- Führe Befehle aus einem Skript aus und schreibe die Befehle in die Konsole:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript</span>

- Starte eine interaktive Eingabeaufforderung, in der jeder Befehl ausgegeben wird, bevor er ausgeführt wird:

`zsh --verbose`

- Führe einen Befehl innerhalb von Zsh mit ausgeschalteten Glob-Mustern aus:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>
