---
layout: page
title: common/ag (português (Brasil))
description: "The Silver Searcher. Parecido com o ack, mas com um foco em ser ainda mais rápido."
content_hash: a77205b30008f308757f4ef438d1b7fd0d7f19e7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

The Silver Searcher. Parecido com o ack, mas com um foco em ser ainda mais rápido.
Mais informações: <https://github.com/ggreer/the_silver_searcher>.

- Acha arquivos que contém "foo" e imprime as linhas correspondentes no contexto:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Acha arquivos que contém "foo" em um diretório específico:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Acha arquivos que contém "foo", mas lista somente os nomes dos arquivos:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Acha arquivos que contém "FOO" sem diferença de caixa e imprime somente o correspondente em vez de a linha inteira:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Acha "foo" em arquivos cujo nome corresponde a "bar":

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Acha arquivos cujo conteúdo corresponde à expressão regular:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- Acha arquivos cujo nome corresponde a "foo":

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
