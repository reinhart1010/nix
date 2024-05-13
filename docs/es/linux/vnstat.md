---
layout: page
title: linux/vnstat (español)
description: "Monitor de tráfico de red de línea de comandos."
content_hash: 319f0a47967fc1d66be318688aa571f7896ff8e1
last_modified_at: 2024-05-13
related_topics:
  - title: English version
    url: /en/linux/vnstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vnstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vnstat

Monitor de tráfico de red de línea de comandos.
Más información: <https://manned.org/vnstat>.

- Muestra un resumen de tráfico de todas las interfaces:

`vnstat`

- Muestra un resumen de tráfico de una interfaz de red específica:

`vnstat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>

- Muestra estadísticas en vivo de una interfaz de red específica:

`vnstat -l -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>

- Muestra estadísticas de tráfico por hora durante las últimas 24 horas mediante un gráfico de barras:

`vnstat -hg`

- Mide y muestra el tráfico promedio por 30 segundos:

`vnstat -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
