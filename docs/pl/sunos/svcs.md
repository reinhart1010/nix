---
layout: page
title: sunos/svcs (polski)
description: "Wyświetl informację o uruchomionych usługach."
content_hash: 205c991647666d9fb897930c4d834286b3ff70d8
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

Wyświetl informację o uruchomionych usługach.
Więcej informacji: <https://www.unix.com/man-page/linux/1/svcs>.

- Wyświetl wszystkie uruchomione usługi:

`svcs`

- Wyświetl wszystkie usługi, które nie są uruchomione:

`svcs -vx`

- Wyświetl informację o usłudze:

`svcs apache`

- Pokaż lokalizację pliku dziennika usługi:

`svcs -L apache`

- Wyświetl koniec pliku dziennika usługi:

`tail $(svcs -L apache)`
