---
layout: page
title: common/fish (Deutsch)
description: "The Friendly Interactive SHell."
content_hash: 36f1f4993439a07073c2690231546c01ddd2f816
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fish.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fish.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fish

The Friendly Interactive SHell.
Eine benutzerfreundliche Eingabeaufforderung.
Weitere Informationen: <https://fishshell.com>.

- Starte eine interaktive Shell-Sitzung:

`fish`

- Starte eine interaktive Shell-Sitzung ohne die Start-Konfiguration zu laden:

`fish --no-config`

- Führe einen bestimmten Befehl aus:

`fish --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'fish wird ausgeführt'</span>`"`

- Führe ein bestimmtes Skript aus:

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript.fish</span>

- Überprüfe ein bestimmtes Skript auf Syntaxfehler:

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript.fish</span>

- Starte eine private, interaktive Shell-Sitzung, in der `fish` weder auf die Shell-History zugreift, noch diese verändert:

`fish --private`

- Definiere und exportiere eine Umgebungsvariable, die über mehrere Shell-Neustarts hinweg existiert (builtin):

`set --universal --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variablenname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variablenwert</span>
