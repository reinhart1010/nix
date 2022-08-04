---
layout: page
title: common/javac (português (Brasil))
description: "O compilador de aplicações Java."
content_hash: 83880fd0647af88595d4f15ad5e6ea8980f222c5
related_topics:
  - title: English version
    url: /en/common/javac.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/javac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javac.html
    icon: bi bi-globe
---
# javac

O compilador de aplicações Java.
Mais informações: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/javac.html>.

- Compile um arquivo `.java`:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.java</span>

- Compile vários arquivos `.java`:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo2.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo3.java</span>

- Compile todos os arquivos `.java` no diretório atual:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- Compile um arquivo `.java` e coloque a classe resultante em um diretório específico:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/algum/diretorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.java</span>
