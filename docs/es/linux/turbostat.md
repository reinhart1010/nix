---
layout: page
title: linux/turbostat (español)
description: "Informa de la topología del procesador, frecuencia, temperatura, potencia y estadísticas de inactividad."
content_hash: c2e03acace142e71d567a237a4a988d2d524afb6
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/linux/turbostat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# turbostat

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
