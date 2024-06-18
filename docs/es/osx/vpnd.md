---
layout: page
title: osx/vpnd (español)
description: "Escucha las conexiones VPN entrantes."
content_hash: fb78613fd52d94a4c82caa5c16362cf4054106e9
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/osx/vpnd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vpnd

Escucha las conexiones VPN entrantes.
No debería ejecutar el programa manualmente.
Más información: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Inicia el daemon:

`vpnd`

- Ejecuta el daemon en primer plano:

`vpnd -x`

- Ejecuta el daemon en primer plano e imprime los registros en la terminal:

`vpnd -d`

- Ejecuta el daemon en primer plano, imprime los registros en la terminal y termina después de validar los argumentos:

`vpnd -n`

- Ejecuta el daemon para una configuración de servidor específica:

`vpnd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_servidor</span>

- Muestra ayuda:

`vpnd -h`
