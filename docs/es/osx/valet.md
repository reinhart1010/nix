---
layout: page
title: osx/valet (español)
description: "Un entorno de desarrollo Laravel que permite alojar sitios a través de túneles locales en `http://<ejemplo>.test`."
content_hash: 386bc4c3842ca33ba6b01c624eba97df320fbee0
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/osx/valet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# valet

Un entorno de desarrollo Laravel que permite alojar sitios a través de túneles locales en `http://<ejemplo>.test`.
Más información: <https://laravel.com/docs/valet>.

- Inicia el daemon valet:

`valet start`

- Registra el directorio de trabajo actual como ruta en la que Valet debe buscar sitios:

`valet park`

- Muestra las rutas 'aparcadas':

`valet paths`

- Sirve un único sitio en lugar de un directorio completo:

`valet link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_aplicacion</span>

- Comparte un proyecto a través de un túnel Ngrok:

`valet share`
