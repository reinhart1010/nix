---
layout: page
title: windows/choco-install (polski)
description: "Instalacja jednej lub więcej paczek zarządzanych przez Chocolatey."
content_hash: b18df74682e829af107458d4d8b802b67ca44bbd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/choco-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-install.html
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

Instalacja jednej lub więcej paczek zarządzanych przez Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-install>.

- Instalacja jednego lub więcej pakietów (oddzielonych spacją):

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu(pakietów)</span>

- Instakacja pakietów z użyciem podanego pliku konfiguracyjnego:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/plik_konfiguracyjny.config</span>

- Instalacja podanej specyfikacji nuspec lub pliku nupkg:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Instalacja konkretnej podanej wersji pakietu:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wersja</span>

- Zezwól na instalacjie wielu wersji danego pakietu:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --allow-multiple`

- Automatyczna akceptacja wszystkich monitów podczas instalacji:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --yes`

- Ustawienie określonego źródła/repozytorium pakietów:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika}</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
