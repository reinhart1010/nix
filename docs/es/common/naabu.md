---
layout: page
title: common/naabu (español)
description: "Un rápido escáner de puertos escrito en Go con un enfoque en la fiabilidad y la simplicidad."
content_hash: ac4174cd841f53fdc05c6e92b292c4469b4b75e7
last_modified_at: 2024-02-09
related_topics:
  - title: English version
    url: /en/common/naabu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# naabu

Un rápido escáner de puertos escrito en Go con un enfoque en la fiabilidad y la simplicidad.
Nota: Algunas características solo se activan cuando `naabu` se ejecuta con privilegios del superusuario, como el escaneo SYN.
Más información: <https://github.com/projectdiscovery/naabu>.

- Ejecuta un escaneo SYN contra los puertos predeterminados (top 100) del host remoto:

`sudo naabu -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Muestra las interfaces de red disponibles y la dirección IP pública del host local:

`naabu -interface-list`

- Escanea todos los puertos del host remoto (escaneo CONNECT sin `sudo`):

`naabu -p - -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Escanea los top 1000 puertos del host remoto:

`naabu -top-ports 1000 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Escanea los puertos TCP 80, 443 y UDP 53 del host remoto:

`naabu -p 80,443,u:53 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Muestra el tipo de CDN que utiliza el host remoto, si existe:

`naabu -p 80,443 -cdn -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
