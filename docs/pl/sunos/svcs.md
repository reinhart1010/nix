---
layout: page
title: sunos/svcs (polski)
description: "Wyświetl informację o uruchomionych usługach."
content_hash: 205c991647666d9fb897930c4d834286b3ff70d8
last_modified_at: 2024-05-09
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svcs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svcs

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
