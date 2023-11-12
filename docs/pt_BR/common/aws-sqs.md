---
layout: page
title: common/aws-sqs (português (Brasil))
description: "Cria, apaga, e envia mensagens para filas para o serviço AWS SQS."
content_hash: d3a7fc5ef266c6f3ac037261fbad9b8c5d83f9bc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-sqs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sqs

Cria, apaga, e envia mensagens para filas para o serviço AWS SQS.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html>.

- Lista todas as filas disponíveis:

`aws sqs list-queues`

- Exibe a URL de uma fila específica:

`aws sqs get-queue-url --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>

- Cria uma fila com atributos especificados em arquivo JSON:

`aws sqs create-queue --queue-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>` --attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://caminho/para/arquivos_de_atributos.json</span>

- Envia mensagem específica para uma fila:

`aws sqs send-message --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regiao</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>` --message-body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">corpo_da_mensagem</span>`" --delay-seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inteiro</span>` --message-attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://caminho/para/arquivos_de_atributos.json</span>

- Remove uma mensagem específica de uma fila:

`aws sqs delete-message --queue-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://url_da_fila</span>` --receipt-handle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificado_da_mensagem</span>

- Remove uma fila específica:

`aws sqs delete-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regiao</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>

- Remove todas as mensagens de uma fila específica:

`aws sqs purge-queue --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regiao</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>

- Habilita uma conta AWS específica para enviar mensagens para uma fila:

`aws sqs add-permission --queue-url https://sqs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regiao</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_fila</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_permissao</span>` --aws-account-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_da_conta</span>` --actions SendMessage`
