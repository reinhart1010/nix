---
layout: page
title: linux/patool (español)
description: "Gestor de archivos de almacenamiento."
content_hash: ba2c3ac1903c92b2def3e923f973b5f2b8e6adbd
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/linux/patool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# patool

Gestor de archivos de almacenamiento.
Se pueden crear, extraer, probar, listar, buscar, reempaquetar y comparar varios formatos de archivo.
Más información: <https://github.com/wummel/patool>.

- Extrae un archivo:

`patool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista el contenido de un archivo:

`patool list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Compara el contenido de dos archivos y muestra las diferencias en la salida estándar:

`patool diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Busca una cadena dentro del contenido de un archivo:

`patool search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
