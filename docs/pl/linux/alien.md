---
layout: page
title: linux/alien (polski)
description: "Konwertuje różne pakiety instalacyjne na inne formaty."
content_hash: db62700a23db2c234b147c397b77f695ce3fd98b
last_modified_at: 2023-10-23
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
---
# alien

Konwertuje różne pakiety instalacyjne na inne formaty.
Więcej informacji: <https://manned.org/alien>.

- Konwertuj wskazany plik instalacyjny do formatu Debiana (rozszerenie `.deb`):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Konwertuj wskazany plik instalacyjny do formatu Red Hata (rozszerzenie `.rpm`):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku}`

- Konwertuj wskazany plik instalacyjny do formatu plików instalacyjnych Slackware (rozszerzenie `.tgz`):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Konwertuj wskazany plik instalacyjny do formatu Debiana i zainstaluj go w systemie:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
