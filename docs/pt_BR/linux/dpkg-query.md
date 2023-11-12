---
layout: page
title: linux/dpkg-query (português (Brasil))
description: "Ferramenta que mostra informações dos pacotes instalados."
content_hash: 678713b8a149d79f4c57df9d75ae70ad78bf746e
last_modified_at: 2023-11-12
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

- Exibir os pacotes instalados:

`dpkg-query -l`

- Exibir os pacotes instalados correspondentes ao critério de busca:

`dpkg-query -l '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>`'`

- Exibir todos os arquivos instalados por um pacote:

`dpkg-query -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibir informações sobre um pacote:

`dpkg-query -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
