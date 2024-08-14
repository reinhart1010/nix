---
layout: page
title: common/doppler (español)
description: "Gestiona variables de entorno a través de diferentes entornos usando Doppler."
content_hash: 71b475c3964e9a03db8e350aa902901456f29761
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/common/doppler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doppler

Gestiona variables de entorno a través de diferentes entornos usando Doppler.
Algunos subcomandos como `doppler run` y `doppler secrets` tienen su propia documentación de uso.
Más información: <https://docs.doppler.com/docs/cli>.

- Configura Doppler CLI en el directorio actual:

`doppler setup`

- Configura el proyecto Doppler y la configuración en el directorio actual:

`doppler setup`

- Ejecuta un comando con secretos inyectados en el entorno:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Visualiza la lista de proyectos:

`doppler projects`

- Visualiza los secretos del proyecto actual:

`doppler secrets`

- Abre el panel de control de doppler en el navegador:

`doppler open`
