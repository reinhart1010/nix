---
layout: page
title: common/fish (Deutsch)
description: "The Friendly Interactive SHell."
content_hash: 73e927a9bc91c604e64ae8a2b8fe6e47563a3562
related_topics:
  - title: English version
    url: /en/common/fish.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fish.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fish

The Friendly Interactive SHell.
Eine benutzerfreundliche Eingabeaufforderung.
Weitere Informationen: <https://fishshell.com>.

- Starte eine interaktive Shell-Sitzung:

`fish`

- Führe einen Befehl aus:

`fish -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`"`

- Führe ein Skript aus:

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript.fish</span>

- Überprüfe ein Skript auf Syntaxfehler:

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript.fish</span>

- Starte eine private interaktive Shell-Sitzung, in der `fish` weder auf die Shell-History zugreift, noch diese verändert:

`fish --private`

- Gib die Version von fish aus:

`fish --version`

- Setze und exportiere eine permanente Umgebungsvariable (nur innerhalb der Shell):

`set -Ux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variablenname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variablenwert</span>
