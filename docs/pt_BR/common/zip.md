---
layout: page
title: common/zip (português (Brasil))
description: "Ferramenta de compressão de arquivos em arquivos zip."
content_hash: ed449feaf12cf780bffd6aff836f7f52f58ab660
last_modified_at: 2024-01-07
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

- Adiciona arquivos/diretórios a um arquivo zip específico ([r]ecusivamente):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>

- Remove arquivos de um arquivo zip ([d]eleta):

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>

- Compacta arquivos/diretórios e[x]cluindo arquivos específicos:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/a/ser/excluido</span>

- Compacta arquivos com um nível de compressão específico (0 - o mais baixo, 9 - o mais alto):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>

- Cria um zip encriptado com uma senha específica:

`zip -r -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>

- Compacta arquivos/diretórios para um zip dividido em múltiplas partes (p. ex. partes de 3 GB):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretorio1 caminho/para/arquivo_ou_diretorio2 ...</span>

- Print a specific archive contents:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/comprimido.zip</span>
