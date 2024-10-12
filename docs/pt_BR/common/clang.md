---
layout: page
title: common/clang (português (Brasil))
description: "Compila arquivos fonte escritos em C, C++ e Objective-C. Pode ser usado como um substituto drop-in para GCC."
content_hash: 1b95aba1638eda865f01bc78038347848a4f936e
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/clang.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clang.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clang.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clang.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang

Compila arquivos fonte escritos em C, C++ e Objective-C. Pode ser usado como um substituto drop-in para GCC.
Parte de LLVM.
Mais informações: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compila vários arquivos fonte para um executável:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte1.c caminho/para/arquivo_fonte2.c ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_resultante</span>

- Ativa a saída de todos os erros e avisos:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>` -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável_resultante</span>

- Mostra avisos comuns, faz depuração de símbolos na saída e otimiza sem afetar a depuração:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>` -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--debug</span>` -Og `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_resultante</span>

- Inclui bibliotecas de um caminho diferente:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_resultante</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/cabeçalho</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/biblioteca</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_biblioteca</span>

- Compila o código-fonte na Representação Intermediária (IR) do LLVM:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--assemble</span>` -emit-llvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ll</span>

- Compila o código-fonte em um arquivo objeto sem vincular:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--compile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>

- Otimiza o programa compilado para desempenho:

`clang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte.c</span>` -O`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|fast</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável_resultante</span>

- Exibe a versão:

`clang --version`
