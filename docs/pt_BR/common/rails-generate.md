---
layout: page
title: common/rails-generate (português (Brasil))
description: "Gerar artefatos Rails a partir de um modelo em um projeto existente."
content_hash: cfa8aa0dbc772a8cd51079126ca8bb36ee921fe6
related_topics:
  - title: English version
    url: /en/common/rails-generate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-generate.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rails-generate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
