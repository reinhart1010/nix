---
layout: page
title: common/awk (português (Brasil))
description: "Uma linguagem de programação versátil para trabalhar com arquivos."
content_hash: 9609b7bf66944f4c621c1a11197a9c9d4e6391f1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awk

Uma linguagem de programação versátil para trabalhar com arquivos.
Mais informações: <https://github.com/onetrueawk/awk>.

- Imprime a quinta coluna (também chamada de campo) em um arquivo separado por espaços:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Imprime a segunda coluna das linhas contendo "foo" em um arquivo separado por espaços:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Imprime a última coluna de cada linha em um arquivo, usando vírgula (ao invés de espaço) como separador de campo:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Soma os valores da primeira coluna de um arquivo e imprime o total:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Imprime de três em três linhas a partir da primeira:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Imprime diferentes valores baseado em condições:

`awk '{if ($1 == "foo") print "Correspondência completa foo"; else if ($1 ~ "bar") print "Correspondência parcial bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Imprime todas as linhas em que a 10ª coluna é igual a um dado valor:

`awk '($10 == valor)'`

- Imprime todas as linhas em que o valor da décima coluna está entre um mínimo e um máximo:

`awk '($10 >= valor_minimo && $10 <= valor_maximo)'`
