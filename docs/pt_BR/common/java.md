---
layout: page
title: common/java (português (Brasil))
description: "Inicializador de programas Java."
content_hash: 39d4b2fee905a5b94b99bae41515ff31bff8caab
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/java.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># java

Inicializador de programas Java.
Mais informações: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- Executa um arquivo Java `.class` que contém um método main, usando o nome da classe:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_classe</span>

- Executa um programa Java e usa classes adicionais de terceiros ou definidas pelo usuário:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/classes1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/classes2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_classe</span>

- Executa um programa `.jar`:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo.jar</span>

- Executa um programa `.jar` com o debugger aguardando conexão na porta 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo.jar</span>

- Exiba a versão do JDK, JRE e HotSpot:

`java -version`

- Exiba os comandos disponíveis do Java:

`java -help`
