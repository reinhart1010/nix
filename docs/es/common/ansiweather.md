---
layout: page
title: common/ansiweather (español)
description: "Un script de shell para mostrar las condiciones meteorológicas actuales en tu terminal."
content_hash: 7d06c0eba7c4d0a3bdebe9bcee4be51d595a4d9c
last_modified_at: 2024-06-18
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
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

Un script de shell para mostrar las condiciones meteorológicas actuales en tu terminal.
Más información: <https://github.com/fcambus/ansiweather>.

- Muestra una previsión usando unidades métricas de los siguientes siete días de una ubicación:

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Muestra una previsión de los siguientes cinco días con símbolos e información de luz diurna de tu ubicación actual:

`ansiweather -F -s true -d true`

- Muestra una previsión con los datos de viento y humedad de tu ubicación actual:

`ansiweather -w true -h true`
