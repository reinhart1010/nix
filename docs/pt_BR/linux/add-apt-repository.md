---
layout: page
title: linux/add-apt-repository (português (Brasil))
description: "Gerenciar definições de repositórios APT."
content_hash: bc5620b95ec9a68ff253285dff13cf38bc21dd81
related_topics:
  - title: Deutsch version
    url: /de/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/add-apt-repository.html
    icon: bi bi-globe
---
# add-apt-repository

Gerenciar definições de repositórios APT.
Mais informações: <https://manned.org/apt-add-repository>.

- Adicionar um repositório:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Remover um repositório:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Adicionar um repositório e atualizar o cache do(s) pacote(s) deste repositório:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>

- Adicionar um repositório e habilitar o download do código fonte do(s) pacote(s) deste repositório:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">especificacao_do_repositorio</span>
