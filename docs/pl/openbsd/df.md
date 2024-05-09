---
layout: page
title: openbsd/df (polski)
description: "Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików."
content_hash: 65ce3efcefa617f2e015285beec934b9c4285392
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
Więcej informacji: <https://man.openbsd.org/df.1>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w formie czytelnej dla człowieka (w oparciu o potęgi 1024):

`df -h`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_folderu</span>

- Wyświetl statystyki dotyczące liczby wolnych i wykorzystanych [i]-węzłów:

`df -i`

- Użyj jednostek 1024-bajtowych do zapisu danych przestrzennych:

`df -k`

- Wyświetl informację w [P]rzenośny sposób:

`df -P`
