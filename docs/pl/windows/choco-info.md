---
layout: page
title: windows/choco-info (polski)
description: "Wyświetlanie szczegółowych informacji o pakiecie Chocolatey."
content_hash: 4222d623b9356b8252a389e998dbf4bd8ad2c322
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-info.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-info.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-info.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-info.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-info.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco info

Wyświetlanie szczegółowych informacji o pakiecie Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-info>.

- Wyświetlanie informacji dotyczących podanego pakietu:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyświetlanie informacji dotyczących podanego pakietu zainstalowanego lokalnie:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --local-only`

- Ustawienie określonego źródła/repozytorium pakietów z którego pobrane zostaną informacje:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
