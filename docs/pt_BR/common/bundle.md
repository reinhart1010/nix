---
layout: page
title: common/bundle (português (Brasil))
description: "Gerenciador de dependências da linguagem de programação Ruby."
content_hash: 0973aac4f173b75511bac2b072973e5f84e3db49
last_modified_at: 2023-12-28
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

- Instala todas as gemas definidas no `Gemfile` esperadas no diretório de trabalho:

`bundle install`

- Executa um comando no contexto do pacote atual:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Atualiza todas as gemas respeitando as regras definidas no `Gemfile` e recria o arquivo `Gemfile.lock`:

`bundle update`

- Atualiza uma ou mais gema(s) específicas definidas no `Gemfile`:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema2</span>

- Atualiza uma ou mais gema(s) específicas definidas no `Gemfile` mas somente para a próxima versão de patch:

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema2</span>

- Atualiza todas as gemas do grupo especificado no `Gemfile`:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">desenvolvimento</span>

- Lista gemas instaladas no `Gemfile` com novas versões disponíveis:

`bundle outdated`

- Cria o esqueleto do projeto de uma nova gema:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema</span>
