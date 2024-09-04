---
layout: page
title: common/at (polski)
description: "Jednokrotnie wykonaj polecenia w późniejszym czasie."
content_hash: 35c6fc11aebb19dc2d186fc5600f74d93c0d65d6
last_modified_at: 2024-09-04
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
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
  - title: Nederlands version
    url: /nl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Jednokrotnie wykonaj polecenia w późniejszym czasie.
Usługa atd (lub atrun) powinna być uruchomiona dla rzeczywistych wykonań.
Więcej informacji: <https://manned.org/at>.

- Wykonaj polecenia z `stdin` po upływie 5 minut (naciśnij `Ctrl + D` po zakończeniu):

`at now + 5 minutes`

- Wykonaj polecenie z `stdin` dziś o 10:00:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./zrób_kopię_zapasową_bazy_danych.sh</span>`" | at 1000`

- Wykonaj polecenia z danego pliku w następny wtorek:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` 9:30 PM Tue`
