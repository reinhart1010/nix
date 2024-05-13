---
layout: page
title: linux/vnstati (español)
description: "Genera imágenes PNG compatibles con vnStat."
content_hash: e4aa8fd8509fdaaa58a21a42df9d3cf95dfe8fbb
last_modified_at: 2024-05-13
related_topics:
  - title: English version
    url: /en/linux/vnstati.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vnstati.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vnstati

Genera imágenes PNG compatibles con vnStat.
Más información: <https://manned.org/vnstati>.

- Genera un resumen de los últimos dos meses, días, etc:

`vnstati --summary --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.png</span>

- Genera los 10 días con mayor tráfico de todos los tiempos:

`vnstati --top 10 --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.png</span>

- Genera estadísticas de tráfico mensual de los últimos 12 meses:

`vnstati --months --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.png</span>

- Genera estadísticas de tráfico por hora de las últimas 24 horas:

`vnstati --hours --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_de_red</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.png</span>
