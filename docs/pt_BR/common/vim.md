---
layout: page
title: common/vim (português (Brasil))
description: "Vim (Vi IMproved), é um editor de texto em linha de comando, que fornece muitos modos para diferentes tipos de manipulação de texto."
content_hash: a9038b92e400d6e35e11c07108ca308893e4d412
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># vim

Vim (Vi IMproved), é um editor de texto em linha de comando, que fornece muitos modos para diferentes tipos de manipulação de texto.
Apertando `i` no modo normal entra em modo insert (inserir). Apertando `<Esc>` volta para o modo normal, que permite o uso dos comandos do Vim.
Mais informações: <https://www.vim.org>.

- Abre um arquivo:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo em um número da linha específica:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_da_linha</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre o manual do Vim em visualização:

`:help<Enter>`

- Salva e sai do arquivo atual:

`:wq<Enter>`

- Entra em modo normal e desfaz a última operação:

`<ESC>u`

- Procura por um sequência padrão dentro de um arquivo (aperte `n`/`N` para ir para próxima/anterior sequência padrão):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sequência_padrão_procurada</span>`<Enter>`

- Executa uma substituição por expressão regular no arquivo todo:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substituição</span>`/g<Enter>`

- Mostra os números das linhas:

`:set nu<Enter>`
