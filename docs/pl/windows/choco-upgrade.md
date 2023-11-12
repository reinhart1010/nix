---
layout: page
title: windows/choco-upgrade (polski)
description: "Aktualizacja jednej lub więcej paczek zarządzanych przez Chocolatey."
content_hash: 9d5a239ce3ddd3b36359f550ac682183942f5549
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-upgrade.html
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

Aktualizacja jednej lub więcej paczek zarządzanych przez Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-upgrade>.

- Aktualizacja jednego lub więcej pakietów (oddzielonych spacją):

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet(pakietów)</span>

- Aktualizacja pakietu do konkretnej wersji:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Aktualizacja wszystkich pakietów zarządzanych przez Chocolatey:

`choco upgrade all`

- Uaktualnij wszystkie pakiety z wyjątkiem określonych pakietów rozdzielanych przecinkami:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet(pakietów)</span>`"`

- Automatyczna akceptacja wszystkich monitów podczas aktualizacji pakietu (--yes):

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --yes`

- Ustawienie określonego źródła/repozytorium pakietów:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
