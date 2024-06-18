---
layout: page
title: common/man (português (Brasil))
description: "Formata e exibe páginas de manual."
content_hash: 30d7111e2719e96b4a25d6b5b0236c24ca4a7296
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/man.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/man.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

Formata e exibe páginas de manual.
Mais informações: <https://www.manned.org/man>.

- Exibe a página de manual de um comando:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe a página de manual de um comando da seção 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Lista todas as seções disponíveis para um comando:

`man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe o caminho procurado pelas páginas de manual:

`man --path`

- Exibe a localização de uma página de manual em vez da própria página de manual:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe a página de manual usando uma localidade específica:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localidade</span>

- Procura páginas de manual contendo um termo de pesquisa:

`man -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termo_de_pesquisa</span>`"`
