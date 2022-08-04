---
layout: page
title: common/dirs (Deutsch)
description: "Zuletzt besuchte Ordner anzeigen und verändern."
content_hash: 384da955a989bbd1894b39ee2735aa570b38524d
related_topics:
  - title: English version
    url: /en/common/dirs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirs.html
    icon: bi bi-globe
---
# dirs

Zuletzt besuchte Ordner anzeigen und verändern.
Die Liste der zuletzt besuchten Ordner kann mit `pushd` und `popd` verändert werden.
Weitere Informationen: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Zeige die zuletzt besuchten Ordner durch Leerzeichen getrennt an:

`dirs`

- Zeige die zuletzt besuchten Ordner mit einem Eintrag pro Zeile an:

`dirs -p`

- Zeige den N-ten Eintrag der zuletzt besuchten Ordner an, beginnend mit 0:

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Leere die Liste der zuletzt besuchten Ordner:

`dirs -c`
