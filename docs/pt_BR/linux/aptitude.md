---
layout: page
title: linux/aptitude (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em Debian."
content_hash: f135ccebbedbbb994cd10c1d591a98a349b8f691
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aptitude

Gerenciador de pacotes das distribuições baseadas em Debian.
Mais informações: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `aptitude`):

`aptitude update`

- Instala um novo pacote e suas dependências:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Busca pacotes correspondentes ao critério de busca:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Remove um pacote e todos que dependam dele:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Atualiza os pacotes instalados para as versões mais recentes:

`aptitude upgrade`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`
