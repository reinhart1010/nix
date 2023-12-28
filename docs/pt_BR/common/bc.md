---
layout: page
title: common/bc (português (Brasil))
description: "Uma linguagem de calculadora de precisão arbitrária."
content_hash: 7dd589858a7df80b92cc9bfa1e5a26bca8a1f16c
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Uma linguagem de calculadora de precisão arbitrária.
Veja também: `dc`.
Mais informações: <https://manned.org/man/bc.1>.

- Inicia uma sessão interativa:

`bc`

- Inicia uma sessão interativa com a biblioteca matemática padrão ativada:

`bc --mathlib`

- Calcula uma expressão:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Executa um script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.bc</span>

- Calcula uma expressão com a escala especificada:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Calcula uma função seno/cosseno/arco tangente/logaritmo natural/função exponencial usando `mathlib`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`
