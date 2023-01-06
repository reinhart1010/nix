---
layout: page
title: common/amass-viz (español)
description: "Visualize gathered information in a network graph."
content_hash: aaad0bbc4eb378ea9ac188f639bf3928eb9a14e8
last_modified_at: 2023-01-06
related_topics:
  - title: English version
    url: /en/common/amass-viz.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-viz.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass viz

Visualize gathered information in a network graph.
Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Genere una visualización D3.js basada en datos específicos de la base de datos::

`amass viz -d3 -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_base_de_datos</span>

- Genera un archivo DOT a partir de los datos específicos de la base de datos:

`amass viz -dot -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_base_de_datos</span>

- Genera un archivo en formato Gephi Graph Exchange XML (GEXF) a partir específicos de los datos de la base de datos:

`amass viz -gexf -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_base_de_datos</span>

- Genera un archivo Graphistry JSON a partir de los datos específicos de la base de datos:

`amass viz -graphistry -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_base_de_datos</span>

- Genera un archivo CSV Maltego a partir de los datos específicos de la base de datos:

`amass viz -maltego -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_base_de_datos</span>
