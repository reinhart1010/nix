---
layout: page
title: common/hping3 (español)
description: "Utilidad de ping avanzada que soporta protocolos TCP, UDP y raw IP."
content_hash: c4cb956cdb91c95ca4d6f5c6517110cc2cec5c6d
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/hping3.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hping3.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hping3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hping3

Utilidad de ping avanzada que soporta protocolos TCP, UDP y raw IP.
Mejor correrla con privilegios elevados.
Más información: <https://github.com/antirez/hping>.

- Ping a un destino con 4 solicitudes ping ICMP:

`hping3 --icmp --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Ping a una dirección IP sobre UDP en el puerto 80:

`hping3 --udp --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Escanea el puerto TCP 80, haciéndolo desde el puerto de origen local 5090:

`hping3 --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --baseport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5090</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Traceroute utilizando un escaneado TCP a un puerto de destino específico:

`hping3 --traceroute --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Escanea un conjunto de puertos TCP en una dirección IP específica:

`hping3 --scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,3000,9000</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Realiza un escaneado TCP ACK para comprobar si un equipo dado está vivo:

`hping3 --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --verbose --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>

- Realiza una prueba de carga en el puerto 80:

`hping3 --flood --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_servidor</span>
