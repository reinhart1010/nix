---
layout: page
title: common/dotnet-restore (español)
description: "Restaura las dependencias y herramientas de un proyecto .NET."
content_hash: ac952ce102c0c0c1e7a67c0c7185da9d300c7685
last_modified_at: 2023-11-30
related_topics:
  - title: English version
    url: /en/common/dotnet-restore.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-restore.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet restore

Restaura las dependencias y herramientas de un proyecto .NET.
Más información: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Restaura dependencias para un proyecto o solución .NET en el directorio actual:

`dotnet restore`

- Restaura dependencias para un proyecto o solución .NET en una ubicación específica:

`dotnet restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/proyecto_o_solución</span>

- Restaura dependencias sin almacenar las solicitudes HTTP en caché:

`dotnet restore --no-cache`

- Obliga a todas las dependencias a ser resueltas incluso si la última restauración fue exitosa:

`dotnet restore --force`

- Restaura dependencias usando los orígenes con error como advertencias:

`dotnet restore --ignore-failed-sources`

- Restaura dependencias con un nivel específico de verbosidad:

`dotnet restore --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>
