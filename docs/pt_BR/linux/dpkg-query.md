---
layout: page
title: linux/dpkg-query (português (Brasil))
description: "Ferramenta que mostra informações dos pacotes instalados."
content_hash: 399f6b8a0f0fdb4c11a697fc8272045a52b3ead9
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/dpkg-query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dpkg-query

Ferramenta que mostra informações dos pacotes instalados.
Mais informações: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- Exibe os pacotes instalados:

`dpkg-query -l`

- Exibe os pacotes instalados correspondentes ao critério de busca:

`dpkg-query -l '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>`'`

- Exibe todos os arquivos instalados por um pacote:

`dpkg-query -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe informações sobre um pacote:

`dpkg-query -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
