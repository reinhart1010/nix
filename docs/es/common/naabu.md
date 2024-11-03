---
layout: page
title: common/naabu (español)
description: "Un escáner de puertos rápido, escrito en Go, enfocado en fiabilidad y simplicidad."
content_hash: 30ac79afdfb6afa5207ab58b492292bf69351a9e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/naabu.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># naabu

Un escáner de puertos rápido, escrito en Go, enfocado en fiabilidad y simplicidad.
Vea también: `nmap`.
Nota: Algunas características sólo se activan cuando `naabu` se ejecuta con privilegios de superusuario, como el escaneo SYN.
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

- Ejecuta `nmap` desde `naabu` para contar con funcionalidades adicionales (`nmap` debe estar instalado):

`sudo naabu -v -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -nmap-cli 'nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v -T5 -sC</span>`'`
