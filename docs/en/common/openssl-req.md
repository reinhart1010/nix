---
layout: page
title: common/openssl-req (English)
description: "OpenSSL command to manage PKCS#10 Certificate Signing Requests."
content_hash: b42b0180d8b82ffb9cf5a3ba40688c2b52da7301
---
# openssl req

OpenSSL command to manage PKCS#10 Certificate Signing Requests.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- Generate a certificate signing request to be sent to a certificate authority:

`openssl req -new -sha256 -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.csr</span>

- Generate a self-signed certificate and a corresponding key-pair, storing both in a file:

`openssl req -new -x509 -newkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -keyout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.cert</span>` -subj "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/C=XX/CN=foobar</span>`" -days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">365</span>
