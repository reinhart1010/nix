---
layout: page
title: common/dotnet (español)
description: "Herramienta multiplataforma de línea de comandos para .NET Core."
content_hash: d69cb67e6ddce4e51b3beb8d8f5ff12737e3c230
related_topics:
  - title: Deutsch version
    url: /de/common/dotnet.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dotnet.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dotnet.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dotnet.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet.html
    icon: bi bi-globe
---
# dotnet

Herramienta multiplataforma de línea de comandos para .NET Core.
Algunos subcomandos, como `dotnet build`, tienen su propia documentación de uso.
Más información: <https://docs.microsoft.com/dotnet/core/tools>.

- Inicializa un proyecto .NET nuevo:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_plantilla</span>

- Restaura los paquetes NuGet:

`dotnet restore`

- Compila y ejectura el proyecto .NET en el directorio actual:

`dotnet run`

- Ejecuta una aplicación dotnet empaquetada (solo necesita el entorno en tiempo de ejecución, el resto de los comandos requieren el SDK de .NET Core instalado):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/aplicación.dll</span>
