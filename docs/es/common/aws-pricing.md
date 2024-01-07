---
layout: page
title: common/aws-pricing (español)
description: "Consulta servicios, productos e información de precios de Amazon Web Services."
content_hash: 01a7c76e2d9eea8b8c640aadb3144a237a3d72ae
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/aws-pricing.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws pricing

Consulta servicios, productos e información de precios de Amazon Web Services.
Más información: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- Lista códigos de servicio de una región específica:

`aws pricing describe-services --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Lista atributos para un código de servicio dado en una región específica:

`aws pricing describe-services --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Imprime información de precios para un código de servicio en una región específica:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Lista valores para un atributo específico para un código de servicio en una región específica:

`aws pricing get-attribute-values --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --attribute-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instanceType</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Imprime información de precios para un código de servicio usando filtros por tipo de instancia y ubicación:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --filters "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)</span>`" --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>
