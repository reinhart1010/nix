---
layout: page
title: common/theharvester (español)
description: "Una herramienta diseñada para las primeras etapas en una prueba de penetración."
content_hash: a1cbbb2a2659a1646eabe833480e6a429966c0ea
last_modified_at: 2024-05-14
related_topics:
  - title: English version
    url: /en/common/theharvester.html
    icon: bi bi-globe
tldri18n_status: 2
---
# theHarvester

Una herramienta diseñada para las primeras etapas en una prueba de penetración.
Más información: <https://github.com/laramies/theHarvester>.

- Recopila información sobre un dominio utilizando Google:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>` --source google`

- Recopila información sobre un dominio utilizando varias fuentes:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duckduckgo,bing,crtsh</span>

- Cambia el límite de resultados con los que trabajar:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Guarda el resultado en dos archivos en formato XML y HTML:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_dominio</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo_de_salida</span>

- Muestra ayuda:

`theHarvester --help`
