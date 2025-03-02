---
layout: page
title: netbsd/sed (polski)
description: "Edytuj tekst w sposób skryptowalny."
content_hash: 68f3e1e26b25bc69015a417fbbdea41fc4d9bf17
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/netbsd/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sed.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/netbsd/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edytuj tekst w sposób skryptowalny.
Zobacz także: `awk`, `ed`.
Więcej informacji: <https://man.netbsd.org/sed.1>.

- Zamień wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) na `mango` (podstawowe wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed 's/jabłko/mango/g'`

- Uruchom określony plik (z ang. [f]ile) skryptu i wydrukuj wynik na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sed</span>

- Opóźnij otwieranie każdego pliku, dopóki polecenie zawierające powiązaną funkcję lub flagę `w` nie zostanie zastosowane do linii wejściowej:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sed</span>

- Włącz rozszerzenie GNU re[g]ex:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sed</span>

- Zamień wszystkie wystąpienia `jabłko` (rozszerzone wyrażenie regularne) na `JABŁKO` (rozszerzone wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -E 's/(jabłko)/\U\1/g'`

- Wypisz tylko pierwszą linię do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | sed -n '1p'`

- Zamień wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) na `mango` (podstawowe wyrażenie regularne) w określonym pliku i nadpisz oryginalny plik:

`sed -i 's/jabłko/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu</span>
