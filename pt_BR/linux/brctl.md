---
layout: page
title: linux/brctl (português (Brasil))
description: "Administração de pontes de rede."
content_hash: 8790c2648887dd4be6ad3ce1aaf0cf31201d7179
related_topics:
  - title: English version
    url: /en/linux/brctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brctl.html
    icon: bi bi-globe
---
# brctl

Administração de pontes de rede.
Mais informações: <https://manned.org/brctl>.

- Exibir uma lista com informações das pontes de rede existentes:

`sudo brctl show`

- Cria uma ponte de rede:

`sudo brctl add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>

- Remover uma ponte de rede:

`sudo brctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>

- Adicionar uma interface de rede em uma ponte de rede existente:

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_interface_de_rede</span>

- Remover uma interface de rede de uma ponte de rede existente:

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_interface_de_rede</span>
