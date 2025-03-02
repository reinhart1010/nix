---
layout: page
title: netbsd/df (polski)
description: "Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików."
content_hash: 7d1453167b3194c53e50c6d456f943676823f43a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/df.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/netbsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
Więcej informacji: <https://man.netbsd.org/df.1>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Użyj jednostek czytelnych dla człowieka (z ang. [h]uman) (opartych na potęgach 1024):

`df -h`

- Wyświetl wszystkie pola struktury/struktur zwróconych przez `statvfs`:

`df -G`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Dołącz statystyki dotyczące liczby wolnych i wykorzystanych [i]węzłów:

`df -i`

- Użyj jednostek 1024-bajtowych do wyświetlania danych o przestrzeni dyskowej:

`df -k`

- Wyświetl informację w sposób [P]rzenośny:

`df -P`
