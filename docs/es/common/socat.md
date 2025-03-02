---
layout: page
title: common/socat (español)
description: "Relé polivalente (SOcket CAT)."
content_hash: f7f95ef046a44ca8943e732c3368bff745d19b7b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/socat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/socat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# socat

Relé polivalente (SOcket CAT).
Más información: <http://www.dest-unreach.org/socat/>.

- Escucha un puerto, espera una conexión entrante y transfiere datos a STDIO:

`sudo socat - TCP-LISTEN:8080,fork`

- Escucha en un puerto usando SSL e imprime a STDOUT:

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- Crea una conexión a un host y puerto, transfiere datos en STDIO al host conectado:

`sudo socat - TCP4:www.example.com:80`

- Reenvía los datos entrantes de un puerto local a otro host y puerto:

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

- Envía datos con un esquema de enrutamiento multicast:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Hello Multicast"</span>` | socat - UDP4-DATAGRAM:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">224.0.0.1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>

- Recibe datos de un multicast:

`socat - UDP4-RECVFROM:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
