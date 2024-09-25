---
layout: page
title: common/doggo (español)
description: "Cliente DNS para Humanos."
content_hash: 46b95471cfaa7d4baf39d892ba70c9f59b1f9779
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/doggo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doggo

Cliente DNS para Humanos.
Escrito en Golang.
Más información: <https://github.com/mr-karan/doggo>.

- Realiza una simple búsqueda DNS:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Consulta registros MX usando un servidor de nombres específico:

`doggo MX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codeberg.org</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.2</span>

- Utiliza DNS sobre HTTPS:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://dns.quad9.net/dns-query</span>

- Salida en formato JSON:

`doggo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --json | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.responses[0].answers[].address</span>`'`

- Realiza una búsqueda DNS inversa:

`doggo --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.4.4</span>` --short`
