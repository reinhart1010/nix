---
layout: page
title: freebsd/df (polski)
description: "Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików."
content_hash: 301746a2f9076405913d241a5ea44e0a5c879e14
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/df.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/df.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?df>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Użyj jednostek czytelnych dla człowieka (z ang. [h]uman) (opartych na potęgach 1024) i wyświetl sumę całkowitą:

`df -h -c`

- Użyj jednostek czytelnych dla człowieka (z ang. [H]uman) (opartych na potęgach 1000):

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Dołącz statystyki dotyczące liczby wolnych i wykorzystanych [i]-węzłów wraz z [T]ypami systemów plików:

`df -iT`

- Użyj jednostek 1024-bajtowych do wyświetlania danych o przestrzeni dyskowej:

`df -k`

- Wyświetl informację w sposób [P]rzenośny:

`df -P`
