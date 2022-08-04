---
layout: page
title: common/openssl-ts (English)
description: "OpenSSL command to generate and verify timestamps."
content_hash: 6d4b44b4cd8eb6942476ed13b2006139f83e0db3
---
# openssl ts

OpenSSL command to generate and verify timestamps.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- Generate a SHA-512 timestamp request of a specific file and output to `file.tsq`:

`openssl ts -query -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -sha512 -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsq</span>

- Check the date and metadata of a specific timestamp response file:

`openssl ts -reply -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsr</span>` -text`

- Verify a timestamp request file and a timestamp response file from the server with an SSL certificate file:

`openssl ts -verify -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsr</span>` -queryfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsq</span>` -partial_chain -CAfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>

- Create a timestamp response for request using key and signing certificate and output it to `file.tsr`:

`openssl ts -reply -queryfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsq</span>` -inkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tsakey.pem</span>` -signer tsacert.pem -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tsr</span>
