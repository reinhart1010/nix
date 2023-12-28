---
layout: page
title: common/bzip2 (português (Brasil))
description: "Um compressor de arquivos que utiliza o algoritmo Burrows–Wheeler."
content_hash: 9cbe523da9c44ff9e919c421cffc69953fcc843a
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/bzip2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bzip2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bzip2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzip2

Um compressor de arquivos que utiliza o algoritmo Burrows–Wheeler.
Mais informações: <https://manned.org/bzip2>.

- Compacta um arquivo:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descompacta um arquivo:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.bz2</span>

- Descompacta um arquivo exibindo o conteúdo no terminal:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.bz2</span>

- Testa a integridade de cada arquivo dentro do arquivo compactado:

`bzip2 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.bz2</span>

- Exibe a taxa de compressão para cada arquivo processado com informações detalhadas:

`bzip2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivos_compactados.bz2</span>

- Descompacta um arquivo sobrescrevendo arquivos existentes:

`bzip2 --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.bz2</span>

- Exibe ajuda:

`bzip2 -h`
