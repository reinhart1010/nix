---
layout: page
title: common/vim (português (Brasil))
description: "Vim (Vi IMproved), é um editor de texto em linha de comando, que fornece muitos modos para diferentes tipos de manipulação de texto."
content_hash: ea4ed2b0873f169a731255a920f85499420dc1d4
last_modified_at: 2024-10-15
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

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

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ZZ|:wq<Enter></span>

- Entra em modo normal e desfaz a última operação:

`<Esc>u`

- Procura por um sequência padrão dentro de um arquivo (aperte `n`/`N` para ir para próxima/anterior sequência padrão):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sequência_padrão_procurada</span>`<Enter>`

- Executa uma substituição por expressão regular no arquivo todo:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substituição</span>`/g<Enter>`

- Mostra os números das linhas:

`:set nu<Enter>`
