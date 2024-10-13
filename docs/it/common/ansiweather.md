---
layout: page
title: common/ansiweather (italiano)
description: "Uno script per mostrare le attuali condizioni meteo nel tuo terminale."
content_hash: a4534a47c306bdf3c5c59b5932d0422266cb60e7
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansiweather

Uno script per mostrare le attuali condizioni meteo nel tuo terminale.
Maggiori informazioni: <https://github.com/fcambus/ansiweather>.

- Mostra una previsione usando unità SI per i prossimi cinque giorni in Rzeszow (Polonia):

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Mostra una previsione con simboli e informazioni sulla luce solare per la tua posizione attuale:

`ansiweather -F -s true -d true`

- Mostra una previsione con informazioni su vento ed umidità per la tua posizione attuale:

`ansiweather -w true -h true`
