---
layout: page
title: common/fmt (português (Brasil))
description: "Reformata um arquivo de texto juntando seus parágrafos e limitando a largura da linha a um determinado número de caracteres (75 por padrão)."
content_hash: 8f87923f51aafc1143bd5325436d37aa58a8c94d
related_topics:
  - title: English version
    url: /en/common/fmt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fmt.html
    icon: bi bi-globe
---
# fmt

Reformata um arquivo de texto juntando seus parágrafos e limitando a largura da linha a um determinado número de caracteres (75 por padrão).
Mais informações: <https://www.gnu.org/software/coreutils/fmt>.

- Reformata um arquivo:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo produzindo linhas de saída de (no máximo) `n` caracteres:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo sem unir linhas menores do que a largura fornecida:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo com espaçamento uniforme (1 espaço entre palavras e 2 espaços entre parágrafos):

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
