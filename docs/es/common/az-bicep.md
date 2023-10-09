---
layout: page
title: common/az-bicep (español)
description: "Grupo de comandos de la CLI de Bicep."
content_hash: ed3b19dc0313e9b7f9a0af7304b014fe933819e1
last_modified_at: 2023-10-09
related_topics:
  - title: English version
    url: /en/common/az-bicep.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az bicep

Grupo de comandos de la CLI de Bicep.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/cli/azure/bicep>.

- Instala la CLI de Bicep.

`az bicep install`

- Crear un archivo de Bicep:

`az bicep build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bicep</span>

- Intenta descompilar un archivo de plantilla ARM a un archivo de Bicep:

`az bicep decompile --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_plantilla.json</span>

- Actualiza la CLI de Bicep a la última versión:

`az bicep upgrade`

- Muestra la versión instalada de la CLI de Bicep:

`az bicep version`

- Lista todas las versiones disponibles de la CLI de Bicep:

`az bicep list-versions`

- Desinstala la CLI de Bicep:

`az bicep uninstall`
