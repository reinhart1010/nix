---
layout: page
title: osx/bc (português (Brasil))
description: "Linguagem e calculadora com precisão arbitrária."
content_hash: 0986c87ef14b9f0c6ceea3373e21f3dd17b1db42
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Linguagem e calculadora com precisão arbitrária.
Veja também: `dc`.
Mais informações: <https://manned.org/man/freebsd-13.0/bc.1>.

- Iniciar uma sessão interativa:

`bc`

- Iniciar uma sessão interativa com a biblioteca matemática padrão habilitada:

`bc --mathlib`

- Calcular uma expressão:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Executar um script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.bc</span>

- Calcular uma expressão com a escala especificada:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Calcular uma função sine/cosine/arctangent/natural logarithm/exponential usando `mathlib`:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
