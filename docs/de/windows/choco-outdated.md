---
layout: page
title: windows/choco-outdated (Deutsch)
description: "Überprüfe mit Chocolatey, ob Pakete veraltet sind."
content_hash: 5e63c297dac8adb74cc6e577bc47a268d0a76c67
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-outdated.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-outdated.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco outdated

Überprüfe mit Chocolatey, ob Pakete veraltet sind.
Weitere Informationen: <https://chocolatey.org/docs/commands-outdated>.

- Zeige eine Liste von veralteten Paketen im Tabellen-Format:

`choco outdated`

- Ignoriere angeheftete Pakete in der Ausgabe:

`choco outdated --ignore-pinned`

- Gib eine eigene Quelle an, mit der die Aktualität der Pakete überprüft wird:

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>
