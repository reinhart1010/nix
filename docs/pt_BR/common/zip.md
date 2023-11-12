---
layout: page
title: common/zip (português (Brasil))
description: "Ferramenta de compressão de arquivos em arquivos zip."
content_hash: 53d8949ecadfb516e8093a1d8a3cd2983281bfc0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

Ferramenta de compressão de arquivos em arquivos zip.
Mais informações: <https://manned.org/zip>.

- Compactando arquivos em um arquivo zip:

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo3</span>

- Compactando todos os arquivos de um diretório:

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/diretorio/*</span>

- Adicionando arquivos a um arquivo zip existente:

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_existente.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/diretorio</span>

- Compactando todos os arquivos de um diretório mantendo estruturas de diretórios:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/diretorio</span>

- Compactando arquivos de um diretório excluindo arquivos específicos:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/diretorio</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/a/ser/excluido</span>

- Compactando arquivos definindo o nível de compressão [9]:

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/diretorio</span>

- Deletando arquivos de um arquivo zip:

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.zip</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo/*.ext</span>`"`
