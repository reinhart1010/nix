---
layout: page
title: common/ack (português (Brasil))
description: "Uma ferramenta de pesquisa similar ao grep, otimizada para programadores."
content_hash: 197a3224c60887fdd584899bb568a4edfe630c58
last_modified_at: 2023-12-28
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ack

Uma ferramenta de pesquisa similar ao grep, otimizada para programadores.
Mais informações: <https://beyondgrep.com/documentation>.

- Procura por arquivos que contenham o termo "foo":

`ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Procura por arquivos em uma linguagem específica:

`ack --ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">each_with_object</span>

- Conta o número total de correspondências para o termo "foo":

`ack -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Mostra o nome dos arquivos contendo o termo "foo" e o número de correspondências em cada arquivo:

`ack -cl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
