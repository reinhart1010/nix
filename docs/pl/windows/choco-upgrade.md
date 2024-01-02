---
layout: page
title: windows/choco-upgrade (polski)
description: "Zaktualizuj jeden lub więcej pakietów Chocolatey."
content_hash: 16336fcb0db1344dda1f479e360939e6673e4932
last_modified_at: 2024-01-02
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

Zaktualizuj jeden lub więcej pakietów Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-upgrade>.

- Zaktualizuj jeden lub więcej pakietów (oddzielonych spacją):

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet1 pakiet2 ...</span>

- Zaktualizuj pakiet do konkretnej wersji:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wersja</span>

- Zaktualizuj wszystkie pakiety:

`choco upgrade all`

- Zaktualizuj wszystkie pakiety z wyjątkiem tych podanych, rozdzielanych przecinkami:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet1 pakiet2 ...</span>`"`

- Automatycznie akceptuj wszystkie monity podczas aktualizacji pakietu:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --yes`

- Ustaw określone źródło/repozytorium pakietów:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- Podaj nazwę użytkownika i hasło do uwierzytelnienia:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
