---
layout: page
title: common/aws-lambda (português (Brasil))
description: "Linha de comando CLI para o AWS lambda."
content_hash: 7a8f71f1b377dddeef650cc5d0f1f96e552bd4a0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-lambda.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lambda

Linha de comando CLI para o AWS lambda.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Executa uma função:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/a/resposta</span>`.json`

- Executa uma função enviando um payload em formato JSON:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/a/resposta</span>`.json`

- Lista as funções:

`aws lambda list-functions`

- Exibe a configuração de uma função:

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista os aliases de uma função:

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Exibe o configuração de concorrência reservada de uma função:

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista quais serviços AWS pode invocar a função:

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
