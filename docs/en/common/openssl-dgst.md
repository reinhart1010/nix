---
layout: page
title: common/openssl-dgst (English)
description: "OpenSSL command to generate digest values and perform signature operations."
content_hash: 0c116599121243f3651007de16a3db949b17811d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# openssl dgst

OpenSSL command to generate digest values and perform signature operations.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- Calculate the SHA256 digest for a file, saving the result to a specific file:

`openssl dgst -sha256 -binary -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Sign a file using an RSA key, saving the result to a specific file:

`openssl dgst -sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">private_key_file</span>` -sha256 -sigopt rsa_padding_mode:pss -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Verify an RSA signature:

`openssl dgst -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_file</span>` -signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">signature_file</span>` -sigopt rsa_padding_mode:pss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">signature_message_file</span>

- Sign a file using and ECDSA key:

`openssl dgst -sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">private_key_file</span>` -sha256 -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Verify an ECDSA signature:

`openssl dgst -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_file</span>` -signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">signature_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">signature_message_file</span>
