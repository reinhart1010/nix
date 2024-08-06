---
layout: page
title: common/aws-acm (español)
description: "AWS Certificate Manager."
content_hash: 79f2d1b72fd1e44fecaa2a41ed79e775c4eb081b
last_modified_at: 2024-08-06
related_topics:
  - title: English version
    url: /en/common/aws-acm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-acm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws acm

AWS Certificate Manager.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Importa un certificado:

`aws acm import-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_arn</span>` --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado</span>` --private-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_privada</span>` --certificate-chain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_cadena</span>

- Lista certificados:

`aws acm list-certificates`

- Describe un certificado:

`aws acm describe-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_arn</span>

- Solicita un certificado:

`aws acm request-certificate --domain-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` --validation-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">método_de_validación</span>

- Elimina un certificado:

`aws acm delete-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_arn</span>

- Lista validaciones de certificados:

`aws acm list-certificates --certificate-statuses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">estado</span>

- Obtén detalles del certificado:

`aws acm get-certificate --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_arn</span>

- Actualiza las opciones del certificado:

`aws acm update-certificate-options --certificate-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_arn</span>` --options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opciones</span>
