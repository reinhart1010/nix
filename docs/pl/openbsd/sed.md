---
layout: page
title: openbsd/sed (polski)
description: "Edytuj tekst w sposób skryptowalny."
content_hash: 192db27dbe55441dd4c8ffe4d9519de1321a427a
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edytuj tekst w sposób skryptowalny.
Zobacz także: `awk`, `ed`.
Więcej informacji: <https://man.openbsd.org/sed.1>.

- Zastąp wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed 's/jabłko/mango/g'`

- Wykonaj określony plik (z ang. [f]ile) skryptu i wypisz jego wynik do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sed</span>

- Opóźnij otwarcie każdego pliku do momentu, gdy polecenie zawierające powiązaną funkcję lub flagę `w` zostanie zastosowane do linii wejścia:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sed</span>

- Zastąp wszystkie wystąpienia `jabłko` (rozszerzone wyrażenie regularne) przez `JABŁKO` (rozszerzone wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -E 's/(jabłko)/\U\1/g'`

- Wypisz tylko pierwszą linię do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -n '1p'`

- Zastąp wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) w określonym pliku i nadpisz oryginalny plik:

`sed -i 's/jabłko/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
