---
layout: page
title: common/gzip (português (Brasil))
description: "Compacta/descompacta arquivos com compressão gzip (LZ77)."
content_hash: 2e755cfe92d65cf88644fdad2f5afa942a973a9a
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/gzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gzip.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/gzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gzip

Compacta/descompacta arquivos com compressão gzip (LZ77).
Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compacta um arquivo, substituindo-o por uma versão compactada gzip:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_arquivo</span>

- Descompacta um arquivo, substituindo-o pela versão descompactada original:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress caminho/para/arquivo.gz</span>

- Compacta um arquivo, mantendo o arquivo original:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keep caminho/para/arquivo</span>

- Compacta um arquivo definindo o nome do arquivo de saída:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout caminho/para/arquivo</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.gz</span>

- Descompacta um arquivo gzip definindo o nome do arquivo de saída:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descompactado</span>

- Especifica o nível de compactação. 1 é o mais rápido (baixa compressão), 9 é o mais lento (baixa compressão), o nível padrão é 6:

`gzip -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.gz</span>

- Mostra o nome e o percentual de redução para cada arquivo comprimido ou descomprimido:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.gz</span>
