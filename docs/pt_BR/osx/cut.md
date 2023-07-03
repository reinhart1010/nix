---
layout: page
title: osx/cut (português (Brasil))
description: "Recorta campos de `stdin` ou arquivos."
content_hash: c8ab5e8328f9a655f371d7ba7c16bc9e9aa9e959
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
---
# cut

Recorta campos de `stdin` ou arquivos.
Mais informações: <https://manned.org/man/freebsd-13.0/cut.1>.

- Imprime um intervalo específico de caracteres/campos de cada linha:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Imprime um intervalo de cada linha com um delimitador específico:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Imprime um intervalo de cada linha de um arquivo específico:

`cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
