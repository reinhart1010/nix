---
layout: page
title: common/gdu (português (Brasil))
description: "Analisador de uso de disco com interface de console."
content_hash: ad43ad72d3e6efb560f45a979f77a76951c71fb6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/gdu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdu

Analisador de uso de disco com interface de console.
Mais informações: <https://github.com/dundee/gdu>.

- Exibe interativamente o uso de disco do diretório atual:

`gdu`

- Exibe interativamente o uso de disco de um determinado diretório:

`gdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Exibe interativamente o uso de disco de todos os discos montados:

`gdu --show-disks`

- Exibe interativamente o uso de disco do diretório atual, mas ignora alguns subdiretórios:

`gdu --ignore-dirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório1,caminho/para/diretório2,...</span>

- Ignora caminhos por expressão regular:

`gdu --ignore-dirs-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.*[abc]+</span>`'`

- Ignora diretórios ocultos:

`gdu --no-hidden`

- Imprime apenas o resultado, não entra no modo interativo:

`gdu --non-interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Não mostra o progresso no modo não interativo (útil em scripts):

`gdu --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
