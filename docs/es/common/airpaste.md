---
layout: page
title: common/airpaste (español)
description: "Comparte mesages y archivos sobre la misma red usando mDNS."
content_hash: 20564f215973b4e2b9a693e0e17f36da7b6bd32b
last_modified_at: 2023-01-02
related_topics:
  - title: English version
    url: /en/common/airpaste.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airpaste.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/airpaste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airpaste.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airpaste.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airpaste

Comparte mesages y archivos sobre la misma red usando mDNS.
Más información: <https://github.com/mafintosh/airpaste>.

- Espera un mensaje y lo muestra cuando se reciba:

`airpaste`

- Envía un texto:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>` | airpaste`

- Envía un archivo:

`airpaste < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Recibe un archivo:

`airpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea un canal o se une al mismo:

`airpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_canal</span>
