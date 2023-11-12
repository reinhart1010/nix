---
layout: page
title: windows/choco-upgrade (Deutsch)
description: "Aktualisiere mit Chocolatey ein oder mehrere Pakete."
content_hash: 27e0e307711cb3437a5499698a6ddf1f36aebced
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco upgrade

Aktualisiere mit Chocolatey ein oder mehrere Pakete.
Weitere Informationen: <https://chocolatey.org/docs/commands-upgrade>.

- Aktualisiere ein oder mehrere Pakete, deren Namen mit Leerzeichen getrennt sind:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket(e)</span>

- Aktualisiere auf eine bestimmte Version des Pakets:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Aktualisiere alle Pakete:

`choco upgrade all`

- Aktualisiere alle außer den angegebenen, durch Kommas getrennten Paketen:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket(e)</span>`"`

- Stimme allen Fragen automatisch zu:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --yes`

- Gib eine eigene Quelle an, von der Pakete aktualisiert werden:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url|alias</span>

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>
