---
layout: page
title: sunos/prstat (polski)
description: "Raportuj statystyki aktywnego procesu."
content_hash: f19360a82c475b2eaa9f157cede813475c2f3614
last_modified_at: 2024-05-10
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

`prstat -c -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -s cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
