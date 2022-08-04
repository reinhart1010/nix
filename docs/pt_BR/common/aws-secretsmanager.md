---
layout: page
title: common/aws-secretsmanager (português (Brasil))
description: "Armazena, gerencia, e obtem secrets."
content_hash: 1357f67ac082b27b6a4093f1ea7650f9d8794807
related_topics:
  - title: English version
    url: /en/common/aws-secretsmanager.html
    icon: bi bi-globe
---
# aws secretsmanager

Armazena, gerencia, e obtem secrets.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- Lista secrets armazenados pelo gerenciador de secretes na conta atual:

`aws secretsmanager list-secrets`

- Cria um secret:

`aws secretsmanager create-secret --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descrição_do_secret</span>`" --secret-string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>

- Apaga um secret:

`aws secretsmanager delete-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ou_arn</span>

- Visualiza detalhes de um secret menos pelo texto do secret:

`aws secretsmanager describe-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ou_arn</span>

- Obtẽm o valor do secret (para pegar a última versão do secret não use `--version-stage`):

`aws secretsmanager get-secret-value --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ou_arn</span>` --version-stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão_do_secret</span>

- Alterna o secret imediatamente usando uma função Lambda:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ou_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_da_função_lambda</span>

- Alterna o secret automaticamente a cada 30 dias usando uma função Lambda:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ou_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_da_função_lambda</span>` --rotation-rules AutomaticallyAfterDays=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
