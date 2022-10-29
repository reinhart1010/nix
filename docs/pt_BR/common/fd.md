---
layout: page
title: common/fd (português (Brasil))
description: "Uma alternativa para `find`."
content_hash: 89dd865e9ab3d41965b9f744cde389d6d0c3b0b3
related_topics:
  - title: English version
    url: /en/common/fd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fd

Uma alternativa para `find`.
Visa ser mais rápido e fácil de usar do que `find`.
Mais informações: <https://github.com/sharkdp/fd>.

- Encontra recursivamente arquivos que correspondam ao padrão fornecido no diretório atual:

`fd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>

- Encontra arquivos que começam com `foo`:

`fd '^foo'`

- Encontra arquivos com uma extensão específica:

`fd --extension txt`

- Encontra arquivos em um diretório específico:

`fd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Inclui arquivos ignorados e ocultos na pesquisa:

`fd --hidden --no-ignore '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>`'`

- Executa um comando em cada resultado de pesquisa retornado:

`fd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>`' --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
