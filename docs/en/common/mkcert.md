---
layout: page
title: common/mkcert (English)
description: "Make locally-trusted development certificates."
content_hash: 27b42d3ca6da54cf6d85d09c19d15475224c259a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# mkcert

Make locally-trusted development certificates.
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
