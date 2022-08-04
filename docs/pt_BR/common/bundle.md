---
layout: page
title: common/bundle (português (Brasil))
description: "Gerenciador de dependências da linguagem de programação Ruby."
content_hash: 847b410057ac5a8abb77af586852aa33d75c327d
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bundle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bundle

Gerenciador de dependências da linguagem de programação Ruby.
Mais informações: <https://bundler.io/man/bundle.1.html>.

- Instalar todas as gemas definidas no `Gemfile`:

`bundle install`

- Atualizar todas as gemas, respeitando as regras definidas no `Gemfile`, e recriar o arquivo `Gemfile.lock`:

`bundle update`

- Atualizar uma gema específica definida no `Gemfile`:

`bundle update --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema</span>

- Criar o esqueleto do projeto de uma nova gema:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_gema</span>
