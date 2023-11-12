---
layout: page
title: common/calc (português (Brasil))
description: "Uma calculadora interativa de precisão arbitrária no terminal."
content_hash: b59bf2a7e9a258be4654eff8b5e70bf5bb555e57
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/calc.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/calc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/calc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/calc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/calc.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/calc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/calc.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/calc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calc

Uma calculadora interativa de precisão arbitrária no terminal.
Mais informações: <https://github.com/lcn2/calc>.

- Inicia a `calc` no modo interativo:

`calc`

- Realiza um cálculo no modo não interativo:

`calc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">85 * (36 / 4)</span>`'`

- Realiza um cálculo sem qualquer formatação de saída (para usar com pipes):

`calc -p '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4/3 * pi() * 5^3</span>`'`

- Realiza um cálculo e, em seguida, altera para o modo [i]nterativo:

`calc -i '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqrt(2)</span>`'`

- Inicia `calc` em um [m]odo de permissão específico (0 até 7, o padrão é 7):

`calc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modo</span>

- Exibe uma introdução à `calc`:

`calc help intro`

- Exibe uma visão geral da `calc`:

`calc help overview`

- Abre o manual da `calc`:

`calc help`
