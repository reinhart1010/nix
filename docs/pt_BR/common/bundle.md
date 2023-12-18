---
layout: page
title: common/bundle (português (Brasil))
description: "Gerenciador de dependências da linguagem de programação Ruby."
content_hash: 8e98a7b4e901152e5bf907c11be7b31aea1c04d2
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundle

Gerenciador de dependências da linguagem de programação Ruby.
Mais informações: <https://bundler.io/man/bundle.1.html>.

- Instalar todas as gemas definidas no `Gemfile` esperadas no diretório de trabalho:

`bundle install`

- Executar um comando no contexto do pacote atual:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Atualizar todas as gemas respeitando as regras definidas no `Gemfile` e recriar o arquivo `Gemfile.lock`:

`bundle update`

- Atualizar uma ou mais gema(s) específicas definidas no `Gemfile`:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema2</span>

- Atualizar uma ou mais gema(s) específicas definidas no `Gemfile` mas somente para a próxima versão de patch:

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema2</span>

- Atualizar todas as gemas do grupo especificado no `Gemfile`:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desenvolvimento</span>

- Listar gemas instaladas no `Gemfile` com novas versões disponíveis:

`bundle outdated`

- Criar o esqueleto do projeto de uma nova gema:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema</span>
