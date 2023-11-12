---
layout: page
title: common/rails-generate (português (Brasil))
description: "Gerar artefatos Rails a partir de um modelo em um projeto existente."
content_hash: cfa8aa0dbc772a8cd51079126ca8bb36ee921fe6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rails-generate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-generate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rails generate

Gerar artefatos Rails a partir de um modelo em um projeto existente.
Mais informações: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- Exibir todos os geradores disponíveis:

`rails generate`

- Criar um modelo:

`rails generate model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_classe</span>

- Criar um controlador:

`rails generate controller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_controlador</span>

- Criar uma estrutura completa (modelo, controlador, testes, etc.) para um novo modelo:

`rails generate scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_modelo</span>
