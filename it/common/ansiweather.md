---
layout: page
title: common/ansiweather (italiano)
description: "Uno script per mostrare le attuali condizioni meteo nel tuo terminale."
content_hash: 6b1695af6b7c50b483189b38ccef56c7800e9d85
related_topics:
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
---
# ansiweather

Uno script per mostrare le attuali condizioni meteo nel tuo terminale.
Maggiori informazioni: <https://github.com/fcambus/ansiweather>.

- Mostra una previsione usando unità SI per i prossimi cinque giorni in Rzeszow (Polonia):

`ansiweather -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Mostra una previsione con simboli e informazioni sulla luce solare per la tua posizione attuale:

`ansiweather -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- Mostra una previsione con informazioni su vento ed umidità per la tua posizione attuale:

`ansiweather -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
