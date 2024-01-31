---
layout: page
title: osx/ping (español)
description: "Envía paquetes ICMP ECHO_REQUEST a hosts de la red."
content_hash: 4f02c34c0ad3bf6648997747c43dbc534b8bd2ea
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

Envía paquetes ICMP ECHO_REQUEST a hosts de la red.
Más información: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping al host especificado:

`ping "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`"`

- Ping a un host un número determinado de veces:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping al `host`, especificando el intervalo en `segundos` entre peticiones (por defecto es 1 segundo):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping a `host` sin intentar buscar nombres simbólicos para las direcciones:

`ping -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping al `host` y hace sonar la campana cuando se recibe un paquete (si tu terminal lo soporta):

`ping -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping al `host` y muestra la hora en la que se ha recibido un paquete (esta opción es un añadido de Apple):

`ping --apple-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`
