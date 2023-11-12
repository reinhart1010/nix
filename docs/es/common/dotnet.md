---
layout: page
title: common/dotnet (español)
description: "Herramienta multiplataforma de línea de comandos para .NET Core."
content_hash: 07f459b7f0ce3d4c2380c037cbb91919b0db3e35
last_modified_at: 2023-11-12
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/dotnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotnet

Herramienta multiplataforma de línea de comandos para .NET Core.
Algunos subcomandos, como `dotnet build`, tienen su propia documentación de uso.
Más información: <https://learn.microsoft.com/dotnet/core/tools>.

- Inicializa un proyecto .NET nuevo:

`dotnet new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_plantilla</span>

- Restaura los paquetes NuGet:

`dotnet restore`

- Compila y ejectura el proyecto .NET en el directorio actual:

`dotnet run`

- Ejecuta una aplicación dotnet empaquetada (solo necesita el entorno en tiempo de ejecución, el resto de los comandos requieren el SDK de .NET Core instalado):

`dotnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/aplicación.dll</span>
