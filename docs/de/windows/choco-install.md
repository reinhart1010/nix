---
layout: page
title: windows/choco-install (Deutsch)
description: "Installiere ein oder mehrere Pakete mit Chocolatey."
content_hash: d6a7b375bc10b3b3010462686e3857289d5d8894
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/choco-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-install.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco install

Installiere ein oder mehrere Pakete mit Chocolatey.
Weitere Informationen: <https://chocolatey.org/docs/commands-install>.

- Installiere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket2</span>

- Installiere Pakete aus einer Konfigurationsdatei:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/pakete.config</span>

- Installiere Pakete aus einer `nuspec`- oder `nupkg`-Datei:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Installiere eine bestimmte Version eines Pakets:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Erlaube die gleichzeitige Installation mehrerer Versionen eines Pakets:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --allow-multiple`

- Stimme allen Fragen automatisch zu:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --yes`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url|alias</span>

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>
