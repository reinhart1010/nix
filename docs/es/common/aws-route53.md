---
layout: page
title: common/aws-route53 (español)
description: "CLI para AWS Route53 - Route 53 es un servicio web de Sistema de Nombres de Dominio (DNS) altamente disponible y escalable."
content_hash: 759dd043832ec712cc42c1765203130784214fb1
last_modified_at: 2023-04-26
related_topics:
  - title: English version
    url: /en/common/aws-route53.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws route53

CLI para AWS Route53 - Route 53 es un servicio web de Sistema de Nombres de Dominio (DNS) altamente disponible y escalable.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- Lista todas las zonas alojadas, privadas y públicas:

`aws route53 list-hosted-zones`

- Muestra todos los registros de una zona:

`aws route53 list-resource-record-sets --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>

- Crea una nueva zona pública utilizando un identificador de solicitud para reintentar la operación de forma segura:

`aws route53 create-hosted-zone --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --caller-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_solicitud</span>

- Elimina una zona (si la zona tiene registros SOA y NS no predeterminados, el comando fallará):

`aws route53 delete-hosted-zone --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>

- Prueba la resolución DNS por parte de los servidores de Amazon de una zona determinada:

`aws route53 test-dns-answer --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>`  --record-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --record-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>