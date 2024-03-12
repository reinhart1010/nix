---
layout: page
title: common/bpkg (español)
description: "Un gestor de paquetes para scripts Bash."
content_hash: f7aacda475fe8e0626139e84310da8dd49d5f001
last_modified_at: 2024-03-12
related_topics:
  - title: English version
    url: /en/common/bpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bpkg

Un gestor de paquetes para scripts Bash.
Más información: <https://github.com/bpkg/bpkg>.

- Actualiza el índice local:

`bpkg update`

- Instala un paquete globalmente:

`bpkg install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un paquete en un subdirectorio del directorio actual:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala una versión específica de un paquete de forma global:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>` -g`

- Muestra detalles sobre un paquete específico:

`bpkg show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Ejecuta un comando, especificando opcionalmente sus argumentos:

`bpkg run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumento1 argumento2 ...</span>
