---
layout: page
title: freebsd/pkg (português (Brasil))
description: "Gerenciador de pacotes do FreeBSD."
content_hash: 5d936203e5233f9eb2b3fdc4363c7f522ae9cb55
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/freebsd/pkg.html
    icon: bi bi-globe
  - title: español version
    url: /es/freebsd/pkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/pkg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/pkg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/pkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg

Gerenciador de pacotes do FreeBSD.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?pkg>.

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
