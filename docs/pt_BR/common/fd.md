---
layout: page
title: common/fd (português (Brasil))
description: "Uma alternativa para `find`."
content_hash: 39d69947d517d89b135acf3093a14369dd358dd7
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/fd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fd

Uma alternativa para `find`.
Visa ser mais rápido e fácil de usar do que `find`.
Mais informações: <https://github.com/sharkdp/fd>.

- Encontra recursivamente arquivos que correspondam ao padrão fornecido no diretório atual:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão|regex</span>`"`

- Encontra arquivos que começam com `foo`:

`fd "^foo"`

- Encontra arquivos com uma extensão específica:

`fd --extension txt`

- Encontra arquivos em um diretório específico:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão|regex</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Inclui arquivos ignorados e ocultos na pesquisa:

`fd --hidden --no-ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão|regex</span>`"`

- Executa um comando em cada resultado de pesquisa retornado:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão|regex</span>`" --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
