---
layout: page
title: common/az-devops (español)
description: "Administra organizaciones de Azure DevOps."
content_hash: c543d46046f0ee47431a0fe0005d0dfce5bbe1d4
last_modified_at: 2023-10-09
related_topics:
  - title: English version
    url: /en/common/az-devops.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az devops

Administra organizaciones de Azure DevOps.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/en-us/cli/azure/devops?view=azure-cli-latest>.

- Configura el Token de Acceso Personal (PAT) para iniciar sesión en una organización específica:

`az devops login --organization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_de_la_organización</span>

- Abre un proyecto en el navegador:

`az devops project show --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_proyecto</span>` --open`

- Lista los miembros de un equipo específico que trabaja en un proyecto en particular:

`az devops team list-member --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_proyecto</span>` --team `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_equipo</span>

- Comprueba la configuración actual de la CLI de Azure DevOps:

`az devops configure --list`

- Configura el comportamiento de la CLI de Azure DevOps estableciendo un proyecto predeterminado y una organización predeterminada:

`az devops configure --defaults project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_proyecto</span>` organization=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_de_la_organización</span>
