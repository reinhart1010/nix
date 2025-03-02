---
layout: page
title: common/socat (English)
description: "Multipurpose relay (SOcket CAT)."
content_hash: bc9c2db878a8e6197fa68ae2e13f0f4704431957
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/socat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/socat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# socat

Multipurpose relay (SOcket CAT).
More information: <http://www.dest-unreach.org/socat/>.

- Listen to a port, wait for an incoming connection and transfer data to STDIO:

`sudo socat - TCP-LISTEN:8080,fork`

- Listen on a port using SSL and print to STDOUT:

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- Create a connection to a host and port, transfer data in STDIO to connected host:

`sudo socat - TCP4:www.example.com:80`

- Forward incoming data of a local port to another host and port:

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

- Send data with multicast routing scheme:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Hello Multicast"</span>` | socat - UDP4-DATAGRAM:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">224.0.0.1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>

- Receive data from a multicast:

`socat - UDP4-RECVFROM:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
