---
layout: page
title: linux/avahi-browse (español)
description: "Muestra los servicios y hosts expuestos en la red local a través de mDNS/DNS-SD."
content_hash: e513b03418f0811146045193db7d399752c2ebcc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/avahi-browse.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/avahi-browse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/avahi-browse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avahi-browse

Muestra los servicios y hosts expuestos en la red local a través de mDNS/DNS-SD.
Avahi es compatible con Bonjour (Zeroconf) encontrado en dispositivos Apple.
Más información: <https://www.avahi.org/>.

- Lista los servicios disponibles en la red local junto con sus direcciones y puertos, ignorando los de la máquina local:

`avahi-browse --all --resolve --ignore-local`

- Lista rápidamente los servicios en la red local en formato SSV para scripts:

`avahi-browse --all --terminate --parsable`

- Lista los dominios en el vecindario:

`avahi-browse --browse-domains`

- Limita la búsqueda a un dominio específico:

`avahi-browse --all --domain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>
