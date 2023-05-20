---
layout: page
title: common/aws-cur (español)
description: "Crea, solicita y elimina definiciones de informes de uso de AWS."
content_hash: 2ec6837edd9f486406bd41b79a4e818e27e43ea2
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/aws-cur.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-cur.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/aws-cur.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-cur.html
    icon: bi bi-globe
---
# aws cur

Crea, solicita y elimina definiciones de informes de uso de AWS.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Crea una definición de informe de costes y uso de AWS a partir de un archivo JSON:

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/report_definition.json</span>

- Enumera las definiciones de informes de uso definidas para la cuenta conectada:

`aws cur describe-report-definitions`

- Elimina una definición de informe de uso:

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_region</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>
