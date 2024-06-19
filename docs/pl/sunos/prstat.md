---
layout: page
title: sunos/prstat (polski)
description: "Raportuj statystyki aktywnego procesu."
content_hash: a56e00cc1435e25c3defce40074267b48b31316d
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prstat

Raportuj statystyki aktywnego procesu.
Więcej informacji: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Sprawdź wszystkie procesy i raportuj statystyki posortowane według użycia procesora:

`prstat`

- Sprawdź wszystkie procesy i raportuj statystyki posortowane według użycia pamięci:

`prstat -s rss`

- Raportuj podsumowanie całkowitego użycia dla każdego użytkownika:

`prstat -t`

- Raportuj informacje o pomiarach procesu mikrostanu:

`prstat -m`

- Wypisz 5 najbardziej obciążających procesor procesów co sekundę:

`prstat -c -n 5 -s cpu 1`
