---
layout: page
title: common/gcc (português (Brasil))
description: "Pré-processa e compila arquivos de código fonte C e C++, depois monta-os e vincula-os."
content_hash: 0424f28b0251ae0f89fdc1b20d77a5090f0c32e9
last_modified_at: 2024-11-18
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gcc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gcc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gcc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gcc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcc

Pré-processa e compila arquivos de código fonte C e C++, depois monta-os e vincula-os.
Mais informações: <https://gcc.gnu.org>.

- Compila múltiplos arquivos de código fonte, produzindo um arquivo executável:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte1.c caminho/para/arquivo_fonte2.c ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Ativa a saída de todos os erros e avisos:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável_de_saída</span>

- Mostra avisos comuns, símbolos de depuração na saída, e otimiza sem afetar a depuração:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--debug</span>` -Og `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Inclui bibliotecas de um local diferente:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/header</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/biblioteca</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_biblioteca</span>

- Compila o código fonte para instruções Assembler:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--assemble</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>

- Compila o código fonte sem efetuar vinculação:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--compile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/font.c</span>

- Otimiza o programa compilado para desempenho:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/fonte.c</span>` -O`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|fast</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_de_saída</span>

- Mostra versão:

`gcc --version`
