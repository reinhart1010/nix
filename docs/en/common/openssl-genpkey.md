---
layout: page
title: common/openssl-genpkey (English)
description: "OpenSSL command to generate asymmetric key pairs."
content_hash: 0c40f13b097cdce020931a2640a29e5e560a399a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# openssl genpkey

OpenSSL command to generate asymmetric key pairs.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>.

- Generate an RSA private key of 2048 bits, saving it to a specific file:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>

- Generate an elliptic curve private key using the curve `prime256v1`, saving it to a specific file:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prime256v1</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>

- Generate an `ED25519` elliptic curve private key, saving it to a specific file:

`openssl genpkey -algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ED25519</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>
