---
layout: page
title: common/at (polski)
description: "Wykonuje polecenia o zadanym czasie."
content_hash: 9a538de4e1474fb67e6e25ec287c2dbeb6ae4d02
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
Więcej informacji: <https://man.archlinux.org/man/at.1>.

- Wykonaj za 5 minut polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`at now + 5 minutes`

- Wykonaj o 10:00 rano polecenie podane z wejścia standardowego:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./zrób_backup.sh</span>`" | at 1000`

- Wykonaj polecenia z podanego pliku w najbliższy wtorek o 21:30:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` 9:30 PM Tue`
