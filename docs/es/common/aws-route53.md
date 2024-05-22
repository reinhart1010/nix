---
layout: page
title: common/aws-route53 (español)
description: "CLI para AWS Route53 - Route 53 es un servicio web de Sistema de Nombres de Dominio (DNS) altamente disponible y escalable."
content_hash: ea49494e50789690ca81ba47a4ff0e947bacd036
last_modified_at: 2024-05-22
related_topics:
  - title: English version
    url: /en/common/aws-route53.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws route53

CLI para AWS Route53 - Route 53 es un servicio web de Sistema de Nombres de Dominio (DNS) altamente disponible y escalable.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- Lista todas las zonas alojadas, privadas y públicas:

`aws route53 list-hosted-zones`

- Muestra todos los registros de una zona:

`aws route53 list-resource-record-sets --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_zona</span>

- Crea una nueva zona pública utilizando un identificador de solicitud para reintentar la operación de forma segura:

`aws route53 create-hosted-zone --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --caller-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_solicitud</span>

- Elimina una zona (si la zona tiene registros SOA y NS no predeterminados, el comando fallará):

`aws route53 delete-hosted-zone --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_zona</span>

- Prueba la resolución DNS por parte de los servidores de Amazon de una zona determinada:

`aws route53 test-dns-answer --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_zona</span>` --record-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --record-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>
