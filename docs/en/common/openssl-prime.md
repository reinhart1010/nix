---
layout: page
title: common/openssl-prime (English)
description: "OpenSSL command to compute prime numbers."
content_hash: 3e6f79680af4f2a1c9fe29eec5fd783fcd0c7aaa
---
# openssl prime

OpenSSL command to compute prime numbers.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- Generate a 2048bit prime number and display it in hexadecimal:

`openssl prime -generate -bits 2048 -hex`

- Check if a given number is prime:

`openssl prime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>
