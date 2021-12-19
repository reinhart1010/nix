---
layout: page
title: common/openssl-x509 (English)
description: "OpenSSL command to manage X.509 certificates."
content_hash: 03a5f962ac383cddbf574badde0ccfb7287b04e0
---
# openssl x509

OpenSSL command to manage X.509 certificates.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- Display certificate information:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.crt</span>` -noout -text`

- Display a certificate's expiration date:

`openssl x509 -enddate -noout -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pem</span>

- Convert a certificate between binary DER encoding and textual PEM encoding:

`openssl x509 -inform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">der</span>` -outform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pem</span>` -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_certificate_file</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">converted_certificate_file</span>

- Store a certificate's public key in a file:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_file</span>` -noout -pubkey -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>
