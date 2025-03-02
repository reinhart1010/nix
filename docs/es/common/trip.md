---
layout: page
title: common/trip (español)
description: "Una herramienta de diagnóstico de red."
content_hash: 71de858c4a036046fe50299b1751c249c2408d48
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/trip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trip

Una herramienta de diagnóstico de red.
Combina la funcionalidad de `traceroute` y `ping`.
Diseñada para ayudar en el análisis de problemas de red.
Más información: <https://trippy.rs/>.

- Uso básico con parámetros por defecto:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Rastrea sin requerir privilegios elevados (solo plataformas soportadas):

`trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --unprivileged`

- Rastrea solo con `IPv6`:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --ipv6`

- Rastrea usando el protocolo `udp`:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>

- Utiliza el puerto de destino personalizado `443` para el rastreo `tcp`:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` --target-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- Utiliza el puerto de origen personalizado `5000` para el seguimiento `udp`:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
