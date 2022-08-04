---
layout: page
title: common/openssl-genrsa (English)
description: "OpenSSL command to generate RSA private keys."
content_hash: 351ea211db38507bdce0fddcb6d792e8bb509b21
---
# openssl genrsa

OpenSSL command to generate RSA private keys.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>.

- Generate an RSA private key of 2048 bits to stdout:

`openssl genrsa`

- Save an RSA private key of an arbitrary number of bits to the output file:

`openssl genrsa -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Generate an RSA private key and encrypt it with AES256 (you will be prompted for a passphrase):

`openssl genrsa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-aes256</span>
