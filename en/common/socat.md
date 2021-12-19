---
layout: page
title: common/socat (English)
description: "Multipurpose relay (SOcket CAT)."
content_hash: 4bc2e0a59402182ef39ea7dcba49c0026f658587
---
# socat

Multipurpose relay (SOcket CAT).

- Listen to a port, wait for an incoming connection and transfer data to STDIO:

`socat - TCP-LISTEN:8080,fork`

- Create a connection to a host and port, transfer data in STDIO to connected host:

`socat - TCP4:www.example.com:80`

- Forward incoming data of a local port to another host and port:

`socat TCP-LISTEN:80,fork TCP4:www.example.com:80`
