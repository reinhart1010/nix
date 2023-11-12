---
layout: page
title: common/bat (português (Brasil))
description: "Imprime e concatena arquivos."
content_hash: ff4fe8cf01effa5e255ea6e6f14d63bd51a8474a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/bat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/bat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bat

Imprime e concatena arquivos.
Um clone do `cat` com realce de sintaxe e integração com Git.
Mais informações: <https://github.com/sharkdp/bat>.

- Imprime o conteúdo de um arquivo para a saída padrão:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Concatena o conteúdo de vários arquivos em um arquivo destino:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_destino</span>

- Acrescenta o conteúdo de vários arquivos ao final de um arquivo destino:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_destino</span>

- Numera todas as linhas de saída:

`bat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Realça a sintaxe de um arquivo JSON:

`bat --language json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.json</span>

- Mostra todas as linguagens suportadas:

`bat --list-languages`
