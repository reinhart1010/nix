---
layout: page
title: common/awk (português (Brasil))
description: "Uma linguagem de programação versátil para trabalhar com arquivos."
content_hash: 81f049f113ce41f9640904c55fd58dc96cf39be2
last_modified_at: 2024-10-09
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
  - title: Nederlands version
    url: /nl/common/awk.html
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

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime a segunda coluna das linhas contendo "foo" em um arquivo separado por espaços:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime a última coluna de cada linha em um arquivo, usando vírgula (ao invés de espaço) como separador de campo:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Soma os valores da primeira coluna de um arquivo e imprime o total:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime de três em três linhas a partir da primeira:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime diferentes valores baseado em condições:

`awk '{if ($1 == "foo") print "Correspondência completa foo"; else if ($1 ~ "bar") print "Correspondência parcial bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime todas as linhas em que o valor da décima coluna está entre um mínimo e um máximo:

`awk '($10 >= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_minimo</span>` && $10 <= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_maximo</span>`)'`

- Imprime tabela de usuários com UID >=1000 com cabeçalho e saída formatada, usando dois pontos como separador (`%-20s` significa: alinhamento à esquerda de 20 caracteres, `%6s` significa: alinhamento à direita 6 caracteres):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Nome", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
