---
layout: page
title: linux/flatpak (español)
description: "Construye, instala y ejecuta aplicaciones y tiempos de ejecución flatpak."
content_hash: fcd87139687a5115e814d6cdb36cdd661e38c6f5
last_modified_at: 2024-09-04
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

Construye, instala y ejecuta aplicaciones y tiempos de ejecución flatpak.
Más información: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Ejecuta una aplicación instalada:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Instala una aplicación desde una fuente remota:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Lista las aplicaciones instaladas, ignorando los tiempos de ejecución:

`flatpak list --app`

- Actualiza todas las aplicaciones y tiempos de ejecución instalados:

`flatpak update`

- Añade una fuente remota:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remota</span>

- Elimina una aplicación instalada:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Elimina todas las aplicaciones no utilizadas:

`flatpak remove --unused`

- Muestra información sobre una aplicación instalada:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
