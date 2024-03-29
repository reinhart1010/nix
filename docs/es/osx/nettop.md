---
layout: page
title: osx/nettop (español)
description: "Muestra información actualizada sobre la red."
content_hash: ab3c46562595dc3c039df9ad37e3b52cfbb10198
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/nettop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nettop

Muestra información actualizada sobre la red.
Más información: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- Monitoriza los sockets TCP y UDP de todas las interfaces:

`nettop`

- Monitoriza sockets TCP desde interfaces Loopback:

`nettop -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loopback</span>

- Supervisa un proceso específico:

`nettop -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id|process_name</span>`"`

- Muestra un resumen por proceso:

`nettop -P`

- Imprime 10 muestras de información de red:

`nettop -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Monitoriza los cambios cada 5 segundos:

`nettop -d -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Mientras se ejecuta nettop, lista los comandos interactivos:

`h`

- Muestra ayuda:

`nettop -h`
