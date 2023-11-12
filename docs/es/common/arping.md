---
layout: page
title: common/arping (español)
description: "Descubrir y sondear hosts en una red utilizando el protocolo ARP."
content_hash: 4f920a014723ec6d75fe221755b9e0080df15014
last_modified_at: 2023-11-12
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

Descubrir y sondear hosts en una red utilizando el protocolo ARP.
Útil para el descubrimiento de direcciones MAC.
Más información: <https://github.com/ThomasHabets/arping>.

- Hace ping a un host mediante paquetes de petición ARP:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Hace ping a un host en una interfaz específica:

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Hace ping a un host y detenerse en la primera respuesta:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Hace ping a un host un determinado número de veces:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Emite paquetes de solicitud ARP para actualizar las cachés ARP de los vecinos:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_a_retransmitir</span>

- Detecta direcciones IP duplicadas en la red enviando peticiones ARP con un tiempo de espera de 3 segundos:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_a_verificar</span>
