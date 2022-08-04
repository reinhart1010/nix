---
layout: page
title: common/rbenv (português (Brasil))
description: "Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby."
content_hash: 6e4944cba1be7ab7d13bb5ba6a585eea355b983f
related_topics:
  - title: English version
    url: /en/common/rbenv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rbenv.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rbenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rbenv

Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
Mais informações: <https://github.com/rbenv/rbenv>.

- Instalar uma ou mais versões, separadas por espaço:

`rbenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uma_ou_mais_versoes</span>

- Exibir a lista de versões instaladas:

`rbenv versions`

- Determinar uma versão específica para ser a instalação padrão:

`rbenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Determinar uma versão específica para um projeto. Este comando deve ser executado no diretório do projeto:

`rbenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibir a versão ativa:

`rbenv version`

- Remover uma versão:

`rbenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao</span>

- Exibir todas as versões que contém um determinado executável:

`rbenv whence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executavel</span>
