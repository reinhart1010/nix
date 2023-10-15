---
layout: page
title: common/az-webapp (español)
description: "Administra aplicaciones web alojadas en Azure Cloud Services."
content_hash: 063f8f1bba988fa78cd002af07e8df98d4c9b56e
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/az-webapp.html
    icon: bi bi-globe
---
# az webapp

Administra aplicaciones web alojadas en Azure Cloud Services.
Parte de `azure-cli` (también conocido como `az`)..
Más información: <https://learn.microsoft.com/cli/azure/webapp>.

- Lista los entornos de ejecución disponibles para una aplicación web:

`az webapp list-runtimes --os-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|linux</span>

- Crea una aplicación web:

`az webapp up --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entorno_de_ejecución</span>

- Lista todas las aplicaciones web:

`az webapp list`

- Elimina una aplicación web específica:

`az webapp delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>
