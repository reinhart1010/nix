---
layout: page
title: common/lpr (português (Brasil))
description: "Ferramenta do CUPS para imprimir arquivos."
content_hash: 8436ea7175afde6d69a5a5135da82a13319dfad6
last_modified_at: 2023-12-30
related_topics:
  - title: Deutsch version
    url: /de/common/lpr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpr

Ferramenta do CUPS para imprimir arquivos.
Veja também: `lpstat`, `lpadmin`.
Mais informações: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- Imprime um arquivo na impressora padrão:

`lpr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime 2 cópias:

`lpr -# `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime em uma impressora específica:

`lpr -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime uma única página (p. ex., 2) ou uma faixa de páginas (p. ex., 2-16):

`lpr -o page-ranges=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|2-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime frente e verso em modo retrato (long) ou paisagem (short):

`lpr -o sides=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">two-sided-long-edge|two-sided-short-edge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Define o tamanho da página (mais opções podem estar disponíveis dependendo da configuração):

`lpr -o media=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4|letter|legal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime múltiplas páginas por folha:

`lpr -o number-up=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|4|6|9|16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
