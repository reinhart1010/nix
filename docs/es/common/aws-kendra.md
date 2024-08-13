---
layout: page
title: common/aws-kendra (español)
description: "CLI para AWS Kendra."
content_hash: a3f37fa0e7c398c80f180b4bc1a2bb5b793f6cb3
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/aws-kendra.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws kendra

CLI para AWS Kendra.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- Crea un índice:

`aws kendra create-index --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol_arn</span>

- Lista índices:

`aws kendra list-indexes`

- Describe un índice:

`aws kendra describe-index --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_índice</span>

- Lista fuentes de datos:

`aws kendra list-data-sources`

- Describe una fuente de datos:

`aws kendra describe-data-source --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_fuente_datos</span>

- Lista consultas de búsqueda:

`aws kendra list-query-suggestions --index-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_índice</span>` --query-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_consulta</span>
