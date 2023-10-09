---
layout: page
title: common/az-config (español)
description: "Administra la configuración de Azure CLI."
content_hash: dcb5f6abdd5acc53185898b4622abf3610649618
last_modified_at: 2023-10-09
related_topics:
  - title: Deutsch version
    url: /de/common/az-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/az-config.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az config

Administra la configuración de Azure CLI.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/cli/azure/config>.

- Muestra todas las configuraciones:

`az config get`

- Muestra las configuraciones para una sección específica:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_sección</span>

- Establece una configuración:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_configuración</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Elimina una configuración:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_configuración</span>
