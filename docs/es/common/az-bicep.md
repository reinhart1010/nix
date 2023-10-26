---
layout: page
title: common/az-bicep (español)
description: "Grupo de comandos de la CLI de Bicep."
content_hash: 5b841a75e1ba67d1ecf6dbc140abd0dc2e67e0c8
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/common/az-bicep.html
    icon: bi bi-globe
---
# az bicep

Grupo de comandos de la CLI de Bicep.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/bicep>.

- Instala la CLI de Bicep:

`az bicep install`

- Crea un archivo de Bicep:

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
