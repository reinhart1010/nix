---
layout: page
title: common/mv (español)
description: "Mueve o renombra archivos y directorios."
content_hash: 5587662fa6ba5f568e4a7c77a59a1dc9a10fa8f3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mv

Mueve o renombra archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/mv>.

- Mueve archivos en ubicaciones arbitrarias:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/destino</span>

- Mueve sin solicitar confirmación antes de sobrescribir archivos existentes:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/destino</span>

- Solicita confirmación antes de sobrescribir archivos existentes, independientemente de los permisos del archivo:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/destino</span>

- No sobrescribe archivos existentes en el destino:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/destino</span>

- Mueve archivos en modo detallado, mostrando los archivos después de moverlos:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/destino</span>
