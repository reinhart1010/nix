---
layout: page
title: common/ansiweather (español)
description: "Un script de shell para mostrar las condiciones meteorológicas actuales en tu terminal."
content_hash: 0f76deb4a2f0d5dff58a170060d26fe1cb575705
last_modified_at: 2023-11-12
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

- Muestra una previsión en unidades métricas para los próximos cinco días en Rzeszow, Polonia:

`ansiweather -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Mostrar una previsión con símbolos y datos de la luz del día dada tu ubicación actual:

`ansiweather -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- Muestra una previsión con los datos de viento y humedad dada tu ubicación actual:

`ansiweather -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
