---
layout: page
title: common/az-webapp (español)
description: "Administra aplicaciones web alojadas en Azure Cloud Services."
content_hash: 403cdd17ad5bc9da334cc5b052567007550a8c5d
related_topics:
  - title: English version
    url: /en/common/az-webapp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az webapp

Administra aplicaciones web alojadas en Azure Cloud Services.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/cli/azure/webapp>.

- Lista los entornos de ejecución disponibles para una aplicación web:

`az webapp list-runtimes --os-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|linux</span>

- Crea una aplicación web:

`az webapp up --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entorno_de_ejecución</span>

- Lista todas las aplicaciones web:

`az webapp list`

- Elimina una aplicación web específica:

`az webapp delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>