---
layout: page
title: common/amass-enum (español)
description: "Busca subdominios de un dominio."
content_hash: 8c9841577d3db356d3ef5a9a684b70690f45dde3
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/amass-enum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/amass-enum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-enum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass enum

Busca subdominios de un dominio.
Más información: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Encuentra (pasivamente) subdominios de un [d]ominio:

`amass enum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>

- Encuentra subdominios de un [d]ominio y los verifica activamente intentando resolver los subdominios encontrados:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Realiza una búsqueda de sub[d]ominios por fuerza bruta:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>

- Guarda los resultados en un archivo de texto:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>

- Guarda la salida del terminal en un archivo y otros resultados detallados en un directorio:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichero_de_salida</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>

- Lista todas las fuentes de datos disponibles:

`amass enum -list`
