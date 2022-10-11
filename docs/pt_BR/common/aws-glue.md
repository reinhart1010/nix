---
layout: page
title: common/aws-glue (português (Brasil))
description: "Linha de comando CLI para o AWS Glue."
content_hash: a0c6a0cfe62fa5ae459b72d07263ba4d1f76e47b
related_topics:
  - title: English version
    url: /en/common/aws-glue.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-glue.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws glue

Linha de comando CLI para o AWS Glue.
Define o endpoint público para o servico AWS Glue.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Lista trabalhos:

`aws glue list-jobs`

- Inicia um trabalho:

`aws glue start-job-run --job-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_trabalho</span>

- Inicia um fluxo de trabalho:

`aws glue start-workflow-run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_fluxo_de_trabalho</span>

- Lista os gatilhos:

`aws glue list-triggers`

- Iniciar um gatilho:

`aws glue start-trigger --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_gatilho</span>

- Cria um endpoint de desenvolvimento:

`aws glue create-dev-endpoint --endpoint-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">papel_arn_usado_pelo_endpoint</span>
