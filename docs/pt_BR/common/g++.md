---
layout: page
title: common/g++ (português (Brasil))
description: "Compila arquivos de código fonte C++."
content_hash: 5c27f6a5d28f64e6b1a56abd977a0964dd038223
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/g++.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/g++.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/g++.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/g++.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/g++.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># g++

Compila arquivos de código fonte C++.
Parte do GCC (GNU Compiler Collection).
Mais informações: <https://gcc.gnu.org>.

- Compila um arquivo de código fonte para um binário executável:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Exibe avisos comuns:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.cpp</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Escolha um padrão de linguagem para o qual compilar (C++98/C++11/C++14/C++17):

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.cpp</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++98|c++11|c++14|c++17</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Inclui bibliotecas localizadas em um caminho diferente do arquivo de código fonte:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/cabeçalho</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/biblioteca</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_biblioteca</span>

- Compila e vincula múltiplos arquivos de código fonte em um binário executável:

`g++ -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_1.cpp caminho/para/fonte_2.cpp ...</span>` && g++ -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte_1.o caminho/para/fonte_2.o ...</span>

- Exibe versão:

`g++ --version`
