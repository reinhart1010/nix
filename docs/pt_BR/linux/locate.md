---
layout: page
title: linux/locate (português (Brasil))
description: "Encontre nomes de arquivos rapidamente."
content_hash: 881e0e52c4892de5cd60c1c5ed38940016ff8368
related_topics:
  - title: Deutsch version
    url: /de/linux/locate.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/locate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># locate

Encontre nomes de arquivos rapidamente.
Mais informações: <https://manned.org/locate>.

- Procura por padrões no banco de dados. Nota: o banco de dados é recalculado periodicamente (geralmente semanalmente ou diariamente):

`locate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>

- Procura um arquivo pelo seu nome de arquivo exato(um padrão que não contém caracteres curingas é interpretado como `*pattern*`):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Recalcula o banco de dados. Você precisa fazer se você quiser achar os arquivos recentementes adicionados:

`sudo updatedb`
