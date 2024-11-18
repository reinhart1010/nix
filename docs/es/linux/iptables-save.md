---
layout: page
title: linux/iptables-save (español)
description: "Guarda la configuración IPv4 de `iptables`."
content_hash: 11f14596cefa8f1de0a82e496a242ac503d3b941
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/linux/iptables-save.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/iptables-save.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables-save

Guarda la configuración IPv4 de `iptables`.
Use `ip6tables-save` para hacer lo mismo para IPv6.
Más información: <https://manned.org/iptables-save>.

- Imprime la configuración de `iptables`:

`sudo iptables-save`

- Imprime la configuración de `iptables` de una [t]abla específica:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabla</span>

- Guarda la configuración de `iptables` al archivo:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
