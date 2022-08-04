---
layout: page
title: common/dotnet-publish (español)
description: "Publica una aplicación .NET y sus dependencias en una carpeta para la implementación en un sistema de hospedaje."
content_hash: 5e4f4ba41dc9e6d40170c3e4240d13d3dc78a4f8
related_topics:
  - title: English version
    url: /en/common/dotnet-publish.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dotnet-publish.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/dotnet-publish.html
    icon: bi bi-globe
---
# dotnet publish

Publica una aplicación .NET y sus dependencias en una carpeta para la implementación en un sistema de hospedaje.
Más información: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Compila un proyecto .NET en modo de lanzamiento:

`dotnet publish --configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>

- Publica el entorno de ejecución de .NET Core con la aplicación para un entorno de ejecución específico:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_entorno_en_tiempo_de_ejecución</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>

- Empaqueta la aplicación en un archivo ejecutable unico de una plataforma específica:

`dotnet publish --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_entorno_en_tiempo_de_ejecucución</span>` -p:PublishSingleFile=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>

- Recorta las bibliotecas no usadas para reducir el tamaño de la aplicación:

`dotnet publish --self-contained true --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_entorno_de_tiempo_de_ejecución</span>` -p:PublishTrimmed=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>

- Compila un proyecto .NET sin restaurar las dependencias:

`dotnet publish --no-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>

- Especifica el directorio de salida:

`dotnet publish --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_proyecto</span>
