---
layout: page
title: linux/apk (español)
description: "Herramienta de gestión de paquetes de Alpine Linux."
content_hash: 0481e3434a2e6f73d886e0e511e842ae79bd8f09
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apk

Herramienta de gestión de paquetes de Alpine Linux.
Más información: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Actualiza los índices de repositorio desde todos los repositorios remotos:

`apk update`

- Instala un nuevo paquete:

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Remueve un paquete:

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Repara un paquete o lo actualiza sin modificar dependencias principales:

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca un paquete usando palabras clave:

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabras_clave</span>

- Muestra información sobre un paquete específico:

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
