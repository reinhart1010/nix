---
layout: page
title: common/axel (español)
description: "Acelerador de descargas."
content_hash: dcd9b8b3a34dfcda3e06ce7efe901e7ef6e6cb3a
last_modified_at: 2023-07-16
related_topics:
  - title: English version
    url: /en/common/axel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/axel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/axel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/axel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/axel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/axel.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># axel

Acelerador de descargas.
Protocolos soportados HTTP, HTTPS y FTP.
Más información: <https://github.com/axel-download-accelerator/axel>.

- Descarga un archivo alojado en una URL:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Descarga y especifica un nombre de archivo:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descarga con múltiples conexiones:

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_conexiones</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Busca copias espejo.

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_de_espejos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limita la velocidad de descarga (bytes por segundo):

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidad</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
