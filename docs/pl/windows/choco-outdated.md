---
layout: page
title: windows/choco-outdated (polski)
description: "Sprawdzenie nieaktualnych pakietów zarządzanych przez Chocolatey."
content_hash: 8f871c313b7d8bf55a2b230881aab0087d44ea70
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco outdated

Sprawdzenie nieaktualnych pakietów zarządzanych przez Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-outdated>.

- Wyświetlanie listy nieaktualnych pakietów w formie tabeli:

`choco outdated`

- Pominięcie/ignorowanie obecnie przypiętych pakietów:

`choco outdated --ignore-pinned`

- Ustawienie określonego źródła do sprawdzenia aktualności pakietów:

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url|alias</span>

- Podanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>
