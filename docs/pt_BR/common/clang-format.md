---
layout: page
title: common/clang-format (português (Brasil))
description: "Formata automaticamente código C/C++/Java/JavaScript/Objective-C/Protobuf/C#."
content_hash: 39317474245b55dc21ac34e7577f3aacc43f39a3
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/clang-format.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang-format.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clang-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clang-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clang-format

Formata automaticamente código C/C++/Java/JavaScript/Objective-C/Protobuf/C#.
Mais informações: <https://clang.llvm.org/docs/ClangFormat.html>.

- Formata um arquivo e exibe o resultado para a `stdout` (saída padrão):

`clang-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Formata um arquivo "in-place", ou seja, salvando nele mesmo:

`clang-format -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Formata um arquivo usando um estilo de código predefinido:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Formata um arquivo usando o arquivo `.clang-format` em um dos diretórios pais do arquivo fonte:

`clang-format --style=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Gera um arquivo `.clang-format` personalizado:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` --dump-config > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clang-format</span>
