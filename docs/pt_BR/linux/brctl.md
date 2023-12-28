---
layout: page
title: linux/brctl (português (Brasil))
description: "Administração de pontes de rede."
content_hash: b10ba519b552b0527d189bd53c50e434deb386ae
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/brctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brctl

Administração de pontes de rede.
Mais informações: <https://manned.org/brctl>.

- Exibe uma lista com informações das pontes de rede existentes:

`sudo brctl show`

- Cria uma ponte de rede:

`sudo brctl add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>

- Remove uma ponte de rede:

`sudo brctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>

- Adiciona uma interface de rede em uma ponte de rede existente:

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_interface_de_rede</span>

- Remove uma interface de rede de uma ponte de rede existente:

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_ponte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_interface_de_rede</span>
