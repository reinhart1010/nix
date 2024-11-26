---
layout: page
title: common/ant (português (Brasil))
description: "Apache Ant: compila e administra projetos baseados em Java."
content_hash: 5e0b3a04481ff39b0561f824cef3b45c0e946737
last_modified_at: 2024-11-26
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ant.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ant

Apache Ant: compila e administra projetos baseados em Java.
Mais informações: <https://ant.apache.org>.

- Compila um projeto com o arquivo padrão de build `build.xml`:

`ant`

- Compila um projeto utilizando um arquivo de build diferente do `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_de_build.xml</span>

- Mostra informações sobre possíveis alvos para este projeto:

`ant -p`

- Mostra informações de debug:

`ant -d`

- Executa todos os alvos que não dependem de alvos defeituosos:

`ant -k`
