---
layout: page
title: common/make (português (Brasil))
description: "Ferramenta de execução de tarefas para os destinos descritos no Makefile."
content_hash: 47e552820886160071f5f6f0ecb80f2e8dd7d045
last_modified_at: 2023-11-29
related_topics:
  - title: English version
    url: /en/common/make.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/make.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/make.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/make.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># make

Ferramenta de execução de tarefas para os destinos descritos no Makefile.
Principalmente utilizada para controlar a compilação de um executável a partir do código-fonte.
Mais informações: <https://www.gnu.org/software/make/manual/make.html>.

- Executa o primeiro destino especificado no Makefile (geralmente chamado de "all"):

`make`

- Executa um destino específico:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Executa um destino específico, executando 4 tarefas simultaneamente em paralelo:

`make -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Usa um Makefile específico:

`make --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Executa o make a partir de outro diretório:

`make --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Força a execução de um destino, mesmo que os arquivos de origem não tenham sido alterados:

`make --always-make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Substitui uma variável definida no Makefile:

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variavel</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_valor</span>

- Substitui variáveis definidas no Makefile pelo ambiente:

`make --environment-overrides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>
