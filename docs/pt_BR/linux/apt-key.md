---
layout: page
title: linux/apt-key (português (Brasil))
description: "Gerenciador de chaves utilizado pelo gerenciador de pacotes APT nas distribuições baseadas em Debian."
content_hash: f5395b8b9ef843d53ddae6c9523ef24a6e0374f5
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Gerenciador de chaves utilizado pelo gerenciador de pacotes APT nas distribuições baseadas em Debian.
Mais informações: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Exibe as chaves confiáveis:

`apt-key list`

- Adiciona uma chave na lista de chaves confiáveis:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_da_chave_publica.asc</span>

- Remove uma chave da lista de chaves confiáveis:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>

- Adiciona uma chave remota na lista de chaves confiáveis:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/arquivo.key</span>` | apt-key add -`

- Adiciona uma chave, de um servidor de chaves, na lista de chaves confiáveis:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEYID</span>
