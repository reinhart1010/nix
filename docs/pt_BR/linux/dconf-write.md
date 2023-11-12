---
layout: page
title: linux/dconf-write (português (Brasil))
description: "Escreve valores de chave nos bancos de dados dconf."
content_hash: 5aba5c3da62767c114ec9df0fb6dce56ef7b832a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/dconf-write.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dconf write

Escreve valores de chave nos bancos de dados dconf.
Veja também: `dconf`.
Mais informações: <https://manned.org/dconf>.

- Escreve um valor de chave específico:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Escreve uma string específica como valor de chave:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`'"`

- Escreve um inteiro específico como valor de chave:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`"`

- Escreve um booleano específico como valor de chave:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>`"`

- Escreve um array específico como valor de chave:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "[`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'primeiro', 'segundo', ...</span>`]"`

- Escreve um array vazio específico como valor de chave:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "@as []"`
