---
layout: page
title: common/az-appconfig (español)
description: "Administra configuraciones de aplicaciones en Azure."
content_hash: 4c65fbfdabed6838a28ae56e5092337aba44f67d
last_modified_at: 2023-10-09
related_topics:
  - title: English version
    url: /en/common/az-appconfig.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az appconfig

Administra configuraciones de aplicaciones en Azure.
Parte de `az`, el cliente de línea de comandos para Microsoft Azure.
Más información: <https://learn.microsoft.com/cli/azure/appconfig>.

- Crea una configuración de aplicación:

`az appconfig create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>

- Elimina una configuración de aplicación específica:

`az appconfig delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_configuración</span>

- Lista todas las configuraciones de aplicaciones bajo la suscripción actual:

`az appconfig list`

- Lista todas las configuraciones de aplicaciones bajo un grupo de recursos específico:

`az appconfig list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Muestra las propiedades de una configuración de aplicación:

`az appconfig show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_configuración</span>

- Actualiza una configuración de aplicación específica:

`az appconfig update --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_configuración</span>
