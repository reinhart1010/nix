---
layout: page
title: common/clang-tidy (português (Brasil))
description: "Um linter C/C++ baseado em LLVM para encontrar violações de estilo, bugs e falhas de segurança por meio de análise estática."
content_hash: c52f0c2c3a5a1ecea9929c133a9e3c9a0c84155c
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/clang-tidy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang-tidy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang-tidy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clang-tidy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clang-tidy

Um linter C/C++ baseado em LLVM para encontrar violações de estilo, bugs e falhas de segurança por meio de análise estática.
Mais informações: <https://clang.llvm.org/extra/clang-tidy/>.

- Executa verificações padrão em um arquivo fonte:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.cpp</span>

- Não executa quaisquer verificações além da verificação `cppcoreguidelines` em um arquivo:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.cpp</span>` -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-*,cppcoreguidelines-*</span>

- Lista todas as verificações disponíveis:

`clang-tidy -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>` -list-checks`

- Especifica defines (definições) e includes (inclusões) como opções de compilações (após `--`):

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.cpp</span>` -- -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meu_projeto/include</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">definições</span>
