---
layout: page
title: common/rbenv (português (Brasil))
description: "Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby."
content_hash: 4a398fbd9116e15ac1319cc1d631dc63991b13df
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/rbenv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rbenv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rbenv

Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
Mais informações: <https://github.com/rbenv/rbenv>.

- Instala uma ou mais versões, separadas por espaço:

`rbenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uma_ou_mais_versoes</span>

- Exibe a lista de versões instaladas:

`rbenv versions`

- Determina uma versão específica para ser a instalação padrão:

`rbenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Determina uma versão específica para um projeto. Este comando deve ser executado no diretório do projeto:

`rbenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibe a versão ativa:

`rbenv version`

- Remove uma versão:

`rbenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibe todas as versões que contém um determinado executável:

`rbenv whence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executavel</span>
