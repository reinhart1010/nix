---
layout: page
title: common/pass (Deutsch)
description: "Programm zum Speichern und Lesen von Passwörtern und anderen sensiblen Daten."
content_hash: 45bbb21c6d831f32eabdf9d8ec6e3209cf2049c7
related_topics:
  - title: English version
    url: /en/common/pass.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pass

Programm zum Speichern und Lesen von Passwörtern und anderen sensiblen Daten.
Die Daten sind mit GPG verschlüsselt und werden mit einem Git repository verwaltet.
Weitere Informationen: <https://www.passwordstore.org>.

- Initialisiere oder verschlüssle einen neuen oder bestehenden Speicher mit einer oder mehreren GPG IDs neu:

`pass init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_2</span>

- Speichere das Passwort und zusätzliche Informationen (Str + D auf neuer Zeile zum abschließen):

`pass insert --multiline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Bearbeite einen bestimmten Eintrag:

`pass edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Kopiere das Passwort (die erste Zeile des Eintrags) in die Zwischenablage:

`pass -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Zeige die Baumstruktur des Passwort-Stores an:

`pass`

- Generiere ein neues, zufälliges Passwort mit Länge n und kopiere is in die Zwischenablage:

`pass generate -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Initialisiere ein Git Repository (Alle durch pass durchgeführten Änderungen werden automatisch committed):

`pass git init`

- Führe einen Git-Befehl für den Passwort-Store aus:

`pass git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>
