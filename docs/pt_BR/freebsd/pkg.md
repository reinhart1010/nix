---
layout: page
title: freebsd/pkg (português (Brasil))
description: "Gerenciador de pacotes do FreeBSD."
content_hash: c428832df78c504ea77ad2f4809f289e24230979
last_modified_at: 2023-12-27
related_topics:
  - title: English version
    url: /en/freebsd/pkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/pkg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/pkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/pkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg

Gerenciador de pacotes do FreeBSD.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Instala um novo pacote:

`pkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Remove um pacote:

`pkg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Atualiza todos os pacotes:

`pkg upgrade`

- Procura um pacote:

`pkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave</span>

- Lista os pacotes instalados:

`pkg info`

- Remove dependências desnecessárias:

`pkg autoremove`
