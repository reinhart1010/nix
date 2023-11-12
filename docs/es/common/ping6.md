---
layout: page
title: common/ping6 (español)
description: "Envía paquetes ICMP ECHO_REQUEST (pings) a hosts de la red usando direcciones IPv6."
content_hash: 6fea38fd24a3e2866e6f6213feef5330977430e9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ping6.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping6.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping6

Envía paquetes ICMP ECHO_REQUEST (pings) a hosts de la red usando direcciones IPv6.
Más información: <https://manned.org/ping6>.

- Envía pings a un host:

`ping6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Envía un número específico de pings a un host:

`ping6 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Envía pings a un host, especificando el intervalo de tiempo entre peticiones (por defecto es 1 segundo):

`ping6 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Envía pings a un host sin intentar resolver nombres simbólicos de direcciones:

`ping6 -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Envía pings a un host y emite un sonido cuando un paquete es recibido (si la terminal lo soporta):

`ping6 -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
