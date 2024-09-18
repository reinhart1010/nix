---
layout: page
title: linux/apt-cache (português (Brasil))
description: "Buscador de pacotes para distribuições baseadas no Debian."
content_hash: 555ded6e22fd596bb8d611fe9541621669342ba5
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-cache.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-cache.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-cache.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-cache.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-cache.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-cache.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-cache.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-cache.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-cache

Buscador de pacotes para distribuições baseadas no Debian.
Mais informações: <https://manned.org/apt-cache.8>.

- Busca pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Exibe informações sobre um pacote:

`apt-cache show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Informa a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe as dependências de um pacote:

`apt-cache depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe pacotes dependentes de um determinado pacote:

`apt-cache rdepends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
