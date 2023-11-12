---
layout: page
title: common/dotnet-build (español)
description: "Compila una aplicación .NET y sus dependencias."
content_hash: f7a919fb1209802f2e25268b4500d20d86a51d3d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dotnet-build.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-build.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet build

Compila una aplicación .NET y sus dependencias.
Más información: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Compila el proyecto o solución en el directorio actual:

`dotnet build`

- Compila un proyecto o solución .NET en el modo de depuración:

`dotnet build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/proyecto_o_solución</span>

- Compila en modo de lanzamiento:

`dotnet build --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>

- Compila sin restaurar las dependencias:

`dotnet build --no-restore`

- Compila con un nivel específico de verbosidad:

`dotnet build --verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet|minimal|normal|detailed|diagnostic</span>

- Compila para un tiempo de ejecución específico:

`dotnet build --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_tiempo_de_ejecución</span>

- Especifica el directorio de salida:

`dotnet build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
