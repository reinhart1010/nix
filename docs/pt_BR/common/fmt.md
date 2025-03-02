---
layout: page
title: common/fmt (português (Brasil))
description: "Reformata um arquivo de texto juntando seus parágrafos e limitando a largura da linha a um determinado número de caracteres (75 por padrão)."
content_hash: cbf4bc87bf32849da3ab4bd3891ea98d47ab55be
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/fmt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fmt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fmt

Reformata um arquivo de texto juntando seus parágrafos e limitando a largura da linha a um determinado número de caracteres (75 por padrão).
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- Reformata um arquivo:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo produzindo linhas de saída de (no máximo) `n` caracteres:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo sem unir linhas menores do que a largura fornecida:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reformata um arquivo com espaçamento uniforme (1 espaço entre palavras e 2 espaços entre parágrafos):

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
