---
layout: page
title: common/aws-glue (español)
description: "CLI para AWS Glue."
content_hash: fb573e5b012e63061ad51d623d1f85da3bc651fb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-glue.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-glue.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-glue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws glue

CLI para AWS Glue.
Define el punto de enlace público para el servicio AWS Glue.
Más información: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Lista trabajos:

`aws glue list-jobs`

- Inicia un trabajo:

`aws glue start-job-run --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_trabajo</span>

- Inicia la ejecución de un flujo de trabajo:

`aws glue start-workflow-run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_flujo</span>

- Lista disparadores:

`aws glue list-triggers`

- Inicia un disparador:

`aws glue start-trigger --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_disparador</span>

- Crea un punto final de desarrollo:

`aws glue create-dev-endpoint --endpoint-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_arn_usado_por_puntofinal</span>
