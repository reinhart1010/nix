---
layout: page
title: linux/apt-cache (português (Brasil))
description: "Buscador de pacotes para distribuições baseadas no Debian."
content_hash: edc84f827b57509f660441bcc1ddf3de2c81c182
last_modified_at: 2023-11-12
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
Mais informações: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Buscar pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Exibir informações sobre um pacote:

`apt-cache show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Informar a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibir as dependências de um pacote:

`apt-cache depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibir pacotes dependentes de um determinado pacote:

`apt-cache rdepends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
