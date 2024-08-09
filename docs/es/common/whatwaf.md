---
layout: page
title: common/whatwaf (español)
description: "Detecta y elude cortafuegos de aplicaciones web y sistemas de protección."
content_hash: 63dec1de8e630358cb430e708aed67fad18dcfc1
last_modified_at: 2024-08-09
related_topics:
  - title: English version
    url: /en/common/whatwaf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whatwaf

Detecta y elude cortafuegos de aplicaciones web y sistemas de protección.
Más información: <https://github.com/Ekultek/WhatWaf>.

- Detecta protección en una sola [u]RL, opcionalmente utiliza salida verbose:

`whatwaf --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` --verbose`

- Detecta protección en un [l]ista de URLs en paralelo desde un archivo (una URL por línea):

`whatwaf --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>

- Envía peticiones a través de un proxy y utiliza una lista de carga útil personalizada desde un archivo (una carga útil por línea):

`whatwaf --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --pl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Envía peticiones a través de Tor (Tor debe estar instalado) utilizando cargas personalizadas (separadas por comas):

`whatwaf --tor --payloads '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">carga1,carga2,...</span>`' -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Utiliza un agente de usuario aleatorio, establece el estrangulamiento y el tiempo de espera, envía una solicitud [P]OST y fuerza una conexión HTTPS:

`whatwaf --ra --throttle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` --post --force-ssl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Enumera todos los WAF que se pueden detectar:

`whatwaf --wafs`

- Lista todos los scripts de manipulación disponibles:

`whatwaf --tampers`
