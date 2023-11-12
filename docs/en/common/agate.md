---
layout: page
title: common/agate (English)
description: "A simple server for the Gemini network protocol."
content_hash: 8892a5454a86994c90c36d9b2d8aeed28b2fc8e4
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/agate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/agate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/agate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/agate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agate

A simple server for the Gemini network protocol.
More information: <https://github.com/mbrubeck/agate>.

- Run and generate a private key and certificate:

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/content/</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-US</span>

- Run server:

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`agate -h`
