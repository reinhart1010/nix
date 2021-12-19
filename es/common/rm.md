---
layout: page
title: common/rm (español)
description: "Elimina archivos o directorios."
content_hash: 829473eae75b8d81541a109a48c7216e9fc086fb
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
---
# rm

Elimina archivos o directorios.
Más información: <https://www.gnu.org/software/coreutils/rm>.

- Elimina archivos de ubicaciones arbitrarias:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/otro/archivo</span>

- Elimina, de forma recursiva, un directorio y todos sus subdirectorios:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Elimina un directorio a la fuerza, sin pedir confirmación ni mostrar mensajes de error:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Elimina varios archivos de forma interactiva, solicitando confirmación antes de eliminar cada archivo:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo(s)</span>

- Elimina archivos en modo detallado, imprimiendo un mensaje por cada archivo eliminado:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/directorio/*</span>
