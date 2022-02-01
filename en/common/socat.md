---
layout: page
title: common/socat (English)
description: "Multipurpose relay (SOcket CAT)."
content_hash: c17d89f9333e9fce7d2a0953829fde18150fee6f
---
# socat

Multipurpose relay (SOcket CAT).
More information: <http://www.dest-unreach.org/socat/>.

- Listen to a port, wait for an incoming connection and transfer data to STDIO:

`socat - TCP-LISTEN:8080,fork`

- Create a connection to a host and port, transfer data in STDIO to connected host:

`socat - TCP4:www.example.com:80`

- Forward incoming data of a local port to another host and port:

`socat TCP-LISTEN:80,fork TCP4:www.example.com:80`
