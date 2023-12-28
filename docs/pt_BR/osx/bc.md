---
layout: page
title: osx/bc (português (Brasil))
description: "Linguagem e calculadora com precisão arbitrária."
content_hash: 55ffd9b539f9fba88d30b80ecee43b66dea6626f
last_modified_at: 2023-12-28
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

- Inicia uma sessão interativa:

`bc`

- Inicia uma sessão interativa com a biblioteca matemática padrão habilitada:

`bc --mathlib`

- Calcula uma expressão:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Executa um script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.bc</span>

- Calcula uma expressão com a escala especificada:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Calcula uma função sine/cosine/arctangent/natural logarithm/exponential usando `mathlib`:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
