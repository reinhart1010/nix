---
layout: page
title: osx/vpnd (español)
description: "Escucha las conexiones VPN entrantes."
content_hash: 70d3ba77b754f892b6d7cfde8431a030e41af499
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/vpnd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vpnd

Escucha las conexiones VPN entrantes.
No debe invocarse manualmente.
Más información: <https://www.unix.com/man-page/osx/8/vpnd/>.

- Inicia el daemon:

`vpnd`

- Ejecuta el daemon en primer plano:

`vpnd -x`

- Ejecuta el daemon en primer plano e imprime los registros en el terminal:

`vpnd -d`

- Ejecuta el daemon en primer plano, imprime los registros en el terminal y luego sale tras validar los argumentos:

`vpnd -n`

- Imprime el resumen de uso y sale:

`vpnd -h`

- Ejecuta el daemon para una configuración de servidor específica:

`vpnd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_id</span>
