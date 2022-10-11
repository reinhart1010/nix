---
layout: page
title: common/aws-kinesis (português (Brasil))
description: "CLI oficial da AWS para o serviço de streamin de dados Amazon Kinesis."
content_hash: fb874848e964ab0c90cdb6ef3893a0391cbd5965
related_topics:
  - title: Deutsch version
    url: /de/common/aws-kinesis.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-kinesis.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-kinesis.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws kinesis

CLI oficial da AWS para o serviço de streamin de dados Amazon Kinesis.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Lista todos os streams de uma conta:

`aws kinesis list-streams`

- Escreve um registro para um stream Kinesis:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem_codificaca_em_base64</span>

- Escreve um registro para um stream Kinesis com codificação base64 inline:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minha mensagem não codificada</span>`" | base64 )"`

- Lista os shards disponíveis em um stream:

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Obtém uma iteração de shards para leitura da mensagem mais antiga no shard do stream:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Lê registros de um shard usando uma iteração de um shard:

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iteração</span>
