---
layout: page
title: common/arping (español)
description: "Descubre y sondea hosts en una red utilizando el protocolo ARP."
content_hash: 02ab5029b4ee423263a9f3799587c51215fc8c16
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/arping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arping.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arping.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arping

Descubre y sondea hosts en una red utilizando el protocolo ARP.
Útil para el descubrimiento de direcciones MAC.
Más información: <https://github.com/ThomasHabets/arping>.

- Haz ping a un host mediante paquetes de petición ARP:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Haz ping a un host en una interfaz específica:

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Haz ping a un host y detenerse en la primera respuesta:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Haz ping a un host un determinado número de veces:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Emite paquetes de solicitud ARP para actualizar las cachés ARP de los vecinos:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_a_retransmitir</span>

- Detecta direcciones IP duplicadas en la red enviando peticiones ARP con un tiempo de espera de 3 segundos:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_a_verificar</span>
