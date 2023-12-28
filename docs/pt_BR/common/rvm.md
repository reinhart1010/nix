---
layout: page
title: common/rvm (português (Brasil))
description: "Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby."
content_hash: 60f6b33b632a5ae48ee0b9e261f0d547a9a7bdca
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/rvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rvm

Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
Mais informações: <https://rvm.io>.

- Instala uma ou mais versões separadas por espaço:

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uma_ou_mais_versoes</span>

- Exibe a lista de versões instaladas:

`rvm list`

- Define uma versão específica para ser utilizada temporariamente:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Define uma versão específica para ser a instalação padrão:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Atualiza uma versão já instalada para uma nova versão:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao_atual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_versao</span>

- Remove uma versão mantendo o código fonte:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Remove uma versão e o código fonte:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibe as dependências específicas para o seu sistema operacional:

`rvm requirements`
