---
layout: page
title: common/rvm (português (Brasil))
description: "Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby."
content_hash: 627a3d4c81872325ed89c219504f1e2382184c17
related_topics:
  - title: English version
    url: /en/common/rvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rvm.html
    icon: bi bi-globe
---
# rvm

Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
Mais informações: <https://rvm.io>.

- Instalar uma ou mais versões separadas por espaço:

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uma_ou_mais_versoes</span>

- Exibir a lista de versões instaladas:

`rvm list`

- Definir uma versão específica para ser utilizada temporariamente:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Definir uma versão específica para ser a instalação padrão:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Atualizar uma versão já instalada para uma nova versão:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao_atual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_versao</span>

- Remover uma versão mantendo o código fonte:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Remover uma versão e o código fonte:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibir as dependências específicas para o seu sistema operacional:

`rvm requirements`
