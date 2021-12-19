---
layout: page
title: common/minisign (English)
description: "A dead simple tool to sign files and verify signatures."
content_hash: e6584a29836af3a28f7175b0077bb8521734ead1
related_topics:
  - title: Deutsch version
    url: /de/common/minisign.html
    icon: bi bi-globe
---
# minisign

A dead simple tool to sign files and verify signatures.
More information: <https://jedisct1.github.io/minisign/>.

- Generate a new keypair at the default location:

`minisign -G`

- Sign a file:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sign a file, adding a trusted (signed) and an untrusted (unsigned) comment in the signature:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Untrusted comment</span>`" -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Trusted comment</span>`"`

- Verify a file and the trusted comments in its signature using the specified public key file:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/publickey.pub</span>

- Verify a file and the trusted comments in its signature, specifying a public key as a Base64 encoded literal:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_base64</span>`"`
