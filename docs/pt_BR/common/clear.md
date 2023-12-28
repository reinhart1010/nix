---
layout: page
title: common/clear (português (Brasil))
description: "Limpa a tela do terminal."
content_hash: e8ad0201cb8b4410e7dfe77bf8310c22f6542e74
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

Limpa a tela do terminal.
Mais informações: <https://manned.org/clear>.

- Limpa a tela (equivalente a apertar Control-L no terminal Bash):

`clear`

- Limpa a tela mantendo o buffer de rolagem do terminal:

`clear -x`

- Especifica o tipo de terminal a ser limpado (por padrão é o valor da variável de ambiente `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_do_terminal</span>

- Mostra a versão do `ncurses` usado pelo `clear`:

`clear -V`
