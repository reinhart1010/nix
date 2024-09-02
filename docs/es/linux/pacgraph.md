---
layout: page
title: linux/pacgraph (español)
description: "Dibuja un gráfico de los paquetes instalados a PNG/SVG/GUI/consola."
content_hash: db888393cad473e84acfcd948d371754dd664e0b
last_modified_at: 2024-09-02
related_topics:
  - title: English version
    url: /en/linux/pacgraph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacgraph

Dibuja un gráfico de los paquetes instalados a PNG/SVG/GUI/consola.
Más información: <https://github.com/keenerd/pacgraph>.

- Crea un gráfico SVG y PNG:

`pacgraph`

- Crear un gráfico SVG:

`pacgraph --svg`

- Imprime resumen en la consola:

`pacgraph --console`

- Anula el nombre de archivo/ubicación por defecto (Nota: No especifiques la extensión del archivo):

`pacgraph --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cambia el color de los paquetes que no son dependencias:

`pacgraph --top=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Cambia el color de los paquetes dependientes:

`pacgraph --dep=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Cambia el color de fondo de un gráfico:

`pacgraph --background=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>

- Cambia el color de los enlaces entre paquetes:

`pacgraph --link=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>
