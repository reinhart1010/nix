---
layout: page
title: common/cp (español)
description: "Copia archivos y directorios."
content_hash: 69b34c193ec32eeba40336d546c1987cdb285d16
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Copia archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/cp>.

- Copia un archivo a otra ruta:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo_original.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo_copia.ext</span>

- Copia un archivo a un directorio, manteniendo el nombre del archivo:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/archivo_original.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_destino</span>

- Copia de forma recursiva un directorio y su contenido a otra ruta (si la ruta de destino existe, el directorio se copiará dentro):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_original</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_copia</span>

- Copia de forma recursiva y verbosa un directorio (muestra un listado de los archivos copiados):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_original</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_copia</span>

- Copia archivos de texto a otra ruta de forma interactiva (pregunta al usuario antes de sobreescribir):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_destino</span>

- Copia enlaces simbólicos sin mantener la referencia al original:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enlace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio_destino</span>
