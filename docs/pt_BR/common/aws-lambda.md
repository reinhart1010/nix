---
layout: page
title: common/aws-lambda (português (Brasil))
description: "Usa o AWS Lambda, um serviço de computação para executar código sem provisionar nem gerenciar servidores."
content_hash: d7ff825fe7a1204239fe051324f547a2b5c98992
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/aws-lambda.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-lambda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lambda

Usa o AWS Lambda, um serviço de computação para executar código sem provisionar nem gerenciar servidores.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Executa uma função:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/a/resposta.json</span>

- Executa uma função enviando um payload em formato JSON:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/a/resposta.json</span>

- Lista as funções:

`aws lambda list-functions`

- Exibe a configuração de uma função:

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista os apelidos de uma função:

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Exibe a configuração de concorrência reservada de uma função:

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista quais serviços AWS pode invocar a função:

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
