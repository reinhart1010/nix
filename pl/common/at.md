---
layout: page
title: common/at (polski)
description: "Wykonuje polecenia o zadanym czasie."
content_hash: 0441c063484b3bd683a572cf5143b503c3b1e8d3
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
---
# at

Wykonuje polecenia o zadanym czasie.
Aby działać poprawnie wymaga działającego serwisu atd (lub atrun).
Więcej informacji: <https://manned.org/at>.

- Wykonaj za 5 minut polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`at now + 5 minutes`

- Wykonaj o 10:00 rano polecenie podane z wejścia standardowego:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./zrób_backup.sh</span>`" | at 1000`

- Wykonaj polecenia z podanego pliku w najbliższy wtorek o 21:30:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` 9:30 PM Tue`
