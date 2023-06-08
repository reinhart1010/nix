---
layout: page
title: common/ag (Nederlands)
description: "The Silver Searcher. Zoals ack, maar wil sneller zijn."
content_hash: caa3ef4ef079420f43f32925b52076e0b1649306
last_modified_at: 2023-06-08
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

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ag

The Silver Searcher. Zoals ack, maar wil sneller zijn.
Meer informatie: <https://github.com/ggreer/the_silver_searcher>.

- Zoek bestanden die "foo" bevatten en druk de regelovereenkomsten in context af:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Vind bestanden die "foo" bevatten in een specifieke map:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Vind bestanden die "foo" bevatten, maar vermeld alleen de bestandsnamen:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Vind bestanden die "FOO" niet hoofdlettergevoelig bevatten en druk alleen de overeenkomst af in plaats van de hele regel:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Zoek "foo" in bestanden met een naam die overeenkomt met "bar":

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Vind bestanden waarvan de inhoud overeenkomt met een reguliere expressie:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- Zoek bestanden met een naam die overeenkomt met "foo":

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
