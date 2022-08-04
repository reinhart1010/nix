---
layout: page
title: common/mkcert (English)
description: "Tool for making locally-trusted development certificates."
content_hash: 9e9b94cace7f7a7e384ddde48088029175bf92cd
---
# mkcert

Tool for making locally-trusted development certificates.
More information: <https://github.com/FiloSottile/mkcert>.

- Install the local CA in the system trust store:

`mkcert -install`

- Generate certificate and private key for a given domain:

`mkcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- Generate certificate and private key for multiple domains:

`mkcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myapp.dev</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>

- Generate wildcard certificate and private key for a given domain and its subdomains:

`mkcert "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.it</span>`"`

- Uninstall the local CA:

`mkcert -uninstall`
