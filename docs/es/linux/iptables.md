---
layout: page
title: linux/iptables (español)
description: "Configura tablas, cadenas y reglas del firewall IPv4 del kernel Linux."
content_hash: 32eb6542ffca6a3073d98e92b640942bb6dcfb75
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/linux/iptables.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/iptables.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables

Configura tablas, cadenas y reglas del firewall IPv4 del kernel Linux.
Utiliza `ip6tables` para establecer reglas para el tráfico IPv6. Vea también: `iptables-save`, `iptables-restore`.
Más información: <https://manned.org/iptables>.

- Muestra cadenas, reglas, contadores de paquetes/bytes y números de línea para la tabla de filtros (filter table):

`sudo iptables --verbose --numeric --list --line-numbers`

- Establece la [p]olítica de cadena de la regla :

`sudo iptables --policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla</span>

- [a]ñade una regla a la política de cadena para la IP:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla</span>

- [a]ñade una regla a la política de cadena para la IP teniendo en cuenta el [p]rotocolo y el puerto:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|icmp|...</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla</span>

- Agrega una regla NAT para traducir todo el tráfico desde la subred `192.168.0.0/24` a la IP pública del host:

`sudo iptables --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nat</span>` --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POSTROUTING</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MASQUERADE</span>

- Borra la regla de la cadena:

`sudo iptables --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_línea_de_regla</span>
