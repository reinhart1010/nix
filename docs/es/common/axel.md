---
layout: page
title: common/axel (español)
description: "Acelerador de descargas."
content_hash: 69c6aa213c87c1cf4fad3ba89ef0096514146647
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# axel

Acelerador de descargas.
Protocolos soportados HTTP, HTTPS y FTP.
Más información: <https://github.com/axel-download-accelerator/axel>.

- Descarga un archivo alojado en una URL:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Descarga y especifica un nombre de archivo:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descarga con múltiples conexiones:

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_conexiones</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Busca copias espejo:

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_de_espejos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limita la velocidad de descarga (bytes por segundo):

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidad</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
