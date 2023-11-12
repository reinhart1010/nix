---
layout: page
title: common/chmod (español)
description: "Cambiar los permisos de acceso de un archivo o directorio."
content_hash: 934f579294e42a2e13fafd2a250c5ec8286aed28
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chmod

Cambiar los permisos de acceso de un archivo o directorio.
Más información: <https://www.gnu.org/software/coreutils/chmod>.

- Otorga al [u]suario que es propietario del archivo permiso para [x] ejecutarlo:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Otorga al usuario derechos para leer (r) y escribir (w) un archivo o directorio:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_o_directorio</span>

- Elimina los derechos de ejecución del [g]rupo:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Otorga a todos los usuarios (a) derechos para leer y ejecutar:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Otorga a [o]tros (que no están en el grupo del propietario) los mismos derechos que los del grupo:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Otorga al [g]rupo y a [o]tros el derecho para escribir (w) un directorio y su contenido:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio</span>
