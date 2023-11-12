---
layout: page
title: common/touch (español)
description: "Cambia el tiempo de accesso y modificación de un archivo (atime, mtime)."
content_hash: 852e254a091d1f59c1d9504f366ccd700a29c4eb
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># touch

Cambia el tiempo de accesso y modificación de un archivo (atime, mtime).
Más información: <https://manned.org/man/freebsd-13.1/touch>.

- Crea un archivo nuevo o cambia los tiempos de archivos existentes al tiempo actual:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Establece los tiempos de un archivo a un día y hora específicos:

`touch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Usa los tiempos de un archivo para establecer los tiempos en otro archivo:

`touch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo2</span>
