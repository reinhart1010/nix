---
layout: page
title: osx/valet (español)
description: "Un entorno de desarrollo Laravel que permite alojar sitios a través de túneles locales en `http://<ejemplo>.test`."
content_hash: e53ae4ea29649f4d5da8b7d576771c669213d5a7
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/valet.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># valet

Un entorno de desarrollo Laravel que permite alojar sitios a través de túneles locales en `http://<ejemplo>.test`.
Más información: <https://laravel.com/docs/valet>.

- Inicia el daemon valet:

`valet start`

- Registra el directorio de trabajo actual como ruta en la que Valet debe buscar sitios:

`valet park`

- Ver las rutas 'aparcadas':

`valet paths`

- Sirve un único sitio en lugar de un directorio completo:

`valet link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_aplicacion</span>

- Compartir un proyecto a través de un túnel Ngrok:

`valet share`
