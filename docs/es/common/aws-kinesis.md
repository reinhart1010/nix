---
layout: page
title: common/aws-kinesis (español)
description: "CLI oficial de AWS para los servicios de streaming de datos de Amazon Kinesis."
content_hash: 63f57925bf8ba8f3ef7d1ff191850636706737fe
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/aws-kinesis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws kinesis

CLI oficial de AWS para los servicios de streaming de datos de Amazon Kinesis.
Más información: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Muestra todos los streams de la cuenta:

`aws kinesis list-streams`

- Escribe un registro en un flujo de Kinesis:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_encoded_message</span>

- Escribe un registro en un flujo Kinesis con codificación base64 en línea:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my raw message</span>`" | base64 )"`

- Lista los fragmentos disponibles en un flujo:

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Obtiene un iterador de fragmentos para leer el mensaje más antiguo de un fragmento de flujo:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Lee registros de un fragmento utilizando un iterador de fragmento:

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iterador</span>
