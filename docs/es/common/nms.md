---
layout: page
title: common/nms (español)
description: "Herramienta de línea de comandos que recrea el famoso efecto de desencriptado de datos de la película Sneakers (1992)."
content_hash: 595faaeaad79a32558b8a603fa2f4480f741fb75
related_topics:
  - title: English version
    url: /en/common/nms.html
    icon: bi bi-globe
---
# nms

Herramienta de línea de comandos que recrea el famoso efecto de desencriptado de datos de la película Sneakers (1992).
Más información: <https://github.com/bartobri/no-more-secrets>.

- Desencripta el texto tras presionar una tecla:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hola, Mundo!</span>`" | nms`

- Desencripta la salida inmediatamente, sin esperar a que una tecla sea pulsada:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -la</span>` | nms -a`

- Desencripta el contenido de un archivo, especificando el color de la salida:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | nms -a -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue|white|yellow|black|magenta|green|red</span>

- Limpia la pantalla antes de desencriptar:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | nms -a -c`
