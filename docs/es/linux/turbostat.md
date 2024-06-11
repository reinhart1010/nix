---
layout: page
title: linux/turbostat (español)
description: "Informa de la topología del procesador, frecuencia, temperatura, potencia y estadísticas de inactividad."
content_hash: c2e03acace142e71d567a237a4a988d2d524afb6
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/linux/turbostat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/turbostat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># turbostat

Informa de la topología del procesador, frecuencia, temperatura, potencia y estadísticas de inactividad.
Más información: <https://manned.org/turbostat.8>.

- Muestra las estadísticas cada cinco segundos:

`sudo turbostat`

- Muestra las estadísticas cada cierto número de segundos:

`sudo turbostat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_segundos</span>

- Muestra información sin decodificar ni imprimir la cabecera de configuración del sistema:

`sudo turbostat --quiet`

- Muestra información útil sobre el CPU cada segundo, sin información de cabecera:

`sudo turbostat --quiet --interval 1 --cpu 0-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta_hilos_CPU</span>` --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- Muestra ayuda:

`turbostat --help`
