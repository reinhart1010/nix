---
layout: page
title: common/ag (italiano)
description: "The Silver Searcher. Come `ack`, ma più veloce."
content_hash: 3b69a9db7f6529659f21ac2d3ce350562f281d3f
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
---
# ag

The Silver Searcher. Come `ack`, ma più veloce.
Maggiori informazioni: <https://github.com/ggreer/the_silver_searcher>.

- Trova file contenenti "foo" e mostra le corrisponenti linee contenenti il termine:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Trova file contenenti "foo" in una specifica directory:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Trova file contenenti "foo" elencandone solamente i nomi:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Trova file contenenti "FOO" senza distinguere tra maiuscole e minuscole, e stampa solo il termine trovato piuttosto che l'intera linea:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Trova "foo" in file il quale nome contiene "bar":

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Trova file il quale contenuto soddisfi una determinata espressione regolare:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>`'`

- Trova file il quale nome contiene "foo":

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
