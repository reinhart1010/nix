---
layout: page
title: common/aws-s3-cp (português (Brasil))
description: "Copia arquivos locais ou objetos do S3 para outros diretórios locais ou no S3."
content_hash: cb9aaa8ddb86890674c1b1a1b7021b95e8b641c7
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/aws-s3-cp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws s3 cp

Copia arquivos locais ou objetos do S3 para outros diretórios locais ou no S3.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

- Copia um arquivo local para um bucket específico.

`aws s3 cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/o/arquivo_remoto</span>

- Copia um objeto específico para outro bucket dentro do S3:

`aws s3 cp s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket2</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/o/destino</span>

- Copia um objeto específico do S3 para outro bucket mantendo seu nome original:

`aws s3 cp s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket2</span>

- Copia objetos do S3 para um diretório local recursivamente:

`aws s3 cp s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_bucket</span>` . --recursive`

- Exibe a ajuda:

`aws s3 cp help`
