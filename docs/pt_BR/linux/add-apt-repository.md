---
layout: page
title: linux/add-apt-repository (português (Brasil))
description: "Gerenciar definições de repositórios APT."
content_hash: bfd49bf74d48737196c402e0a4e293339e929bc2
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/add-apt-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# add-apt-repository

Gerenciar definições de repositórios APT.
Mais informações: <https://manned.org/apt-add-repository>.

- Adiciona um repositório:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Remove um repositório:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Adiciona um repositório e atualiza o cache do(s) pacote(s) deste repositório:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Adiciona um repositório e habilita o download do código fonte do(s) pacote(s) deste repositório:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>
