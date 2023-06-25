---
layout: page
title: osx/aiac (español)
description: "Utiliza OpenAI para generar configuraciones IaC, utilidades, consultas y más."
content_hash: 097cf1ba04f3f3b304803d3063ec7aef7fcf50af
last_modified_at: 2023-06-25
related_topics:
  - title: English version
    url: /en/osx/aiac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aiac

Utiliza OpenAI para generar configuraciones IaC, utilidades, consultas y más.
Más información: <https://github.com/gofireflyio/aiac>.

- Genera Terraform para una cuenta de almacenamiento Azure:

`aiac get terraform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">for an azure storage account</span>

- Genera un Dockerfile para nginx:

`aiac get dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">for a secured nginx</span>

- Genera una GitHub action que aplica Terraform:

`aiac get github action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">that plans and applies terraform</span>

- Genera un escáner de puertos en Python:

`aiac get python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code that scans all open ports in my network</span>

- Genera una consulta MongoDB:

`aiac get mongo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query that aggregates all documents by created date</span>
