---
layout: page
title: linux/ac (português (Brasil))
description: "Imprime estatísticas de quanto tempo usuários permaneceram conctados."
content_hash: 6e3af74f039444195224e0354b92fece5cd233f3
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ac

Imprime estatísticas de quanto tempo usuários permaneceram conctados.
Mais informações: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprime quanto tempo em horas o usuário atual ficou conectado:

`ac`

- Imprime quanto tempo em horas usuários ficaram conectados:

`ac --individual-totals`

- Imprime quanto tempo em horas um usuário em particular ficou conectado:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Imprime quanto tempo um usuário em particular ficou conectado em horas por dia (com total):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Também exibe detalhes adicionais:

`ac --compatibility`
