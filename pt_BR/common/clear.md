---
layout: page
title: common/clear (português (Brasil))
description: "Limpa a tela do terminal."
content_hash: 5a43c483469aba0f414cc8dd2991f8306014abba
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
---
# clear

Limpa a tela do terminal.
Mais informações: <https://manned.org/clear>.

- Limpar a tela (equivalente a apertar Control-L no terminal Bash):

`clear`

- Limpar a tela mantendo o buffer de rolagem do terminal:

`clear -x`

- Especificar o tipo de terminal a ser limpado (por padrão é o valor da variável de ambiente `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_do_terminal</span>

- Mostra a versão do `ncurses` usado pelo `clear`:

`clear -V`
