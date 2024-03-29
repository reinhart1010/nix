---
layout: page
title: common/mise (español)
description: "Gestiona versiones de diferentes paquetes."
content_hash: a42af2896713ca1b8847527259f17b18e63fbb21
last_modified_at: 2024-03-07
related_topics:
  - title: English version
    url: /en/common/mise.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mise

Gestiona versiones de diferentes paquetes.
Más información: <https://mise.jdx.dev>.

- Lista todos los complementos disponibles:

`mise plugins list-all`

- Instala un complemento:

`mise plugins add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista las versiones disponibles para instalación:

`mise ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Instala una versión específica de un paquete:

`mise install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Establece una versión global de un paquete:

`mise use --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Establece una versión local de un paquete:

`mise use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Establece una variable de entorno en la configuración:

`mise set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>
