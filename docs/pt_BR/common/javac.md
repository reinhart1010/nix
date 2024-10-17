---
layout: page
title: common/javac (português (Brasil))
description: "O compilador de aplicações Java."
content_hash: 4fde832e239d9032c2b33025c37a862203e7557a
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/javac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/javac.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/javac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javac

O compilador de aplicações Java.
Mais informações: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- Compila um arquivo `.java`:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.java</span>

- Compila vários arquivos `.java`:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1.java arquivo2.java ...</span>

- Compila todos os arquivos `.java` no diretório atual:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- Compila um arquivo `.java` e coloque a classe resultante em um diretório específico:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.java</span>
