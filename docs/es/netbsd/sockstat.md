---
layout: page
title: netbsd/sockstat (español)
description: "Lista sockets abiertos de Internet o dominios UNIX."
content_hash: aa4176a21a15fdaceb55ad3eeae5fc95fdc5ad92
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

Lista sockets abiertos de Internet o dominios UNIX.
Nota: este programa es una reescritura para NetBSD 3.0 de `sockstat` de FreeBSD.
Vea también: `netstat`.
Más información: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Muestra información de sockets IPv4, IPv6 y Unix que estén escuchando y conectados:

`sockstat`

- Muestra información para sockets IPv[4]/IPv[6] escuchando ([l]istening) sobre [p]uertos específicos usando un [P]rotocolo específico:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto1,puerto2...</span>

- También muestra sockets [c]onectados, mostrando sockets [u]nix:

`sockstat -cu`

- Solo muestra salida [n]umérica, sin resolver nombres simbólicos para direcciones y puertos:

`sockstat -n`

- Lista sockets de una [f]amilia de direcciones específica:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>
