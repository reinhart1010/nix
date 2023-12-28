---
layout: page
title: common/node (português (Brasil))
description: "Plataforma de JavaScript para o lado do Servidor (Node.js)."
content_hash: 888b34da9576f1476a8a107443895088d211d0b2
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># node

Plataforma de JavaScript para o lado do Servidor (Node.js).
Mais informações: <https://nodejs.org>.

- Executa um arquivo JavaScript:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>`.js`

- Inicializa a REPL (shell interativa):

`node`

- Executa JavaScript, passando-o no comando:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Executa um arquivo JavaScript, imprimindo o resultado:

`node -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>`"`

- Ativa o inspetor, pausando a execução até que um depurador seja conectado depois que o código-fonte for totalmente analisado:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
