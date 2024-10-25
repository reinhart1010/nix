---
layout: page
title: linux/cp (español)
description: "Copia archivos y directorios."
content_hash: 79efceab55d1fb76fd90d6ff5d4ff3a6605bb3c9
last_modified_at: 2024-10-25
related_topics:
  - title: català version
    url: /ca/linux/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/cp.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Copia archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/cp>.

- Copia un archivo a otro directorio:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_origen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_destino.ext</span>

- Copia un archivo en otro directorio, conservando el nombre del archivo:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archivo_origen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_principal</span>

- Copia de forma recursiva el contenido de un directorio a otra ubicación (si el destino existe, el directorio es copiado en esa ubicación):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_destino</span>

- Copia un directorio de forma recursiva en modo verbose (muestra los archivos a medida que se copian):

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_destino</span>

- Copia varios archivos de inmediato a un directorio:

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Copia todos los archivos con una extensión específica a otra ubicación en modo interactivo (pregunta al usuario antes de sobreescribir):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_destino</span>

- Sigue los enlaces simbólicos antes de copiar:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_destino</span>

- Usa la ruta completa de los archivos de origen, creando los directorios intermedios faltantes al copiar:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta_de_origen/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_destino</span>
