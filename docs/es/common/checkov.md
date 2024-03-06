---
layout: page
title: common/checkov (español)
description: "Checkov es una herramienta de análisis estático de código para Infraestructura como Código (IaC)."
content_hash: bfa1de2b737181aad406d99564184cc8a8aabb12
last_modified_at: 2024-03-06
related_topics:
  - title: English version
    url: /en/common/checkov.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/checkov.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># checkov

Checkov es una herramienta de análisis estático de código para Infraestructura como Código (IaC).
También es una herramienta de análisis de composición de software (SCA) para imágenes y paquetes de código abierto.
Más información: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- Analiza un directorio que contenga IaC (Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile, etc):

`checkov --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Escanea un archivo IaC, omitiendo bloques de código en la salida:

`checkov --compact --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista todas las comprobaciones de todos los tipos de IaC:

`checkov --list`
