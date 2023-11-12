---
layout: page
title: common/pass (Deutsch)
description: "Programm zum Speichern und Lesen von Passwörtern und anderen sensiblen Daten."
content_hash: 45bbb21c6d831f32eabdf9d8ec6e3209cf2049c7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pass

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
