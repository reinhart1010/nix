---
layout: page
title: osx/cut (português (Brasil))
description: "Recorta campos de `stdin` ou arquivos."
content_hash: 700af681c9024f59bfe119011d96af670943c9e2
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Recorta campos de `stdin` ou arquivos.
Mais informações: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- Imprime um intervalo específico de caracteres/campos de cada linha:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Imprime um intervalo de campos de cada linha com um delimitador específico:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Imprime um intervalo de caracteres de cada linha de um arquivo específico:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
