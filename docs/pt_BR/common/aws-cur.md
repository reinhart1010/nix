---
layout: page
title: common/aws-cur (português (Brasil))
description: "Cria, pesquisa e apaga relatórios de uso do AWS."
content_hash: f8ddc8b00d755648a4221c3b71106e8598f632d1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-cur.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cur.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-cur.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/aws-cur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cur

Cria, pesquisa e apaga relatórios de uso do AWS.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Cria um relatório de uso e custo do AWS definido de a partir de um arquivo JSON:

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/definição_do_relatório.json</span>

- Lista as definições dos relatórios de uso para a conta logada:

`aws cur describe-report-definitions`

- Apaga uma definição de relatório de uso:

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">região_aws</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">relatório</span>
