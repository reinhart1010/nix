---
layout: page
title: common/openssl-s_client (English)
description: "OpenSSL command to create TLS client connections."
content_hash: 0c5cffdda585932c867b103bc4353422aa221b31
---
# openssl s_client

OpenSSL command to create TLS client connections.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- Display the start and expiry dates for a domain's certificate:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` 2>/dev/null | openssl x509 -noout -dates`

- Display the certificate presented by an SSL/TLS server:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` </dev/null`

- Set the Server Name Indicator (SNI) when connecting to the SSL/TLS server:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -servername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Display the complete certificate chain of an HTTPS server:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:443 -showcerts </dev/null`
